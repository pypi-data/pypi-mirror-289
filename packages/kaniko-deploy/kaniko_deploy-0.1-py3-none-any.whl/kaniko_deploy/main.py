import base64
import json
import click
import os
import subprocess
import getpass
from pathlib import Path
from kubernetes import client, config

config.load_kube_config()
kube_v1 = client.CoreV1Api()
kube_job_v1 = client.BatchV1Api()

KANIKO_BUILD_TEMPLATE_FILENAME = "kaniko-build-template.yaml"
VOLUME_CLAIM_TEMPLATE_FILENAME = "volume-claim-template.yaml"
VOLUME_TEMPLATE_FILENAME = "volume-template.yaml"
KANIKO_BUILD_FILENAE = "kaniko-build.yaml"

AVAILABLE_CMDS = ["deploy"]


class KanikoBuild:

    def __init__(
        self,
        context_dir,
        docker_filepath,
        no_push,
        docker_username,
        docker_repo,
        docker_pass,
        docker_email=None,
    ):
        self.context_dir = context_dir
        self.docker_filepath = docker_filepath
        self.docker_username = docker_username
        self.docker_repo = docker_repo
        self.docker_email = docker_email
        self.docker_pass = docker_pass
        self.no_push = no_push
        self.pv_flag = False
        self.pvc_flag = False

    def build(self):

        if self.is_ctx_local_dir():
            if self.is_dockerfile_present():
                self.create_volume()
                self.claim_volume()
        if self.no_push == False:
            self.create_kube_secret()
        self.create_pod()

    def is_ctx_local_dir(self):
        if Path(self.context_dir).exists():
            return True
        return False

    def is_dockerfile_present(self):
        docker_filepath = self.context_dir + "/" + self.docker_filepath
        if os.path.exists(docker_filepath) == False:
            raise FileNotFoundError(f"No such dockerfile found: '{docker_filepath}'")
        return True

    def create_volume(self, cap_size=None, volume_name=None):
        self.created_vol_name = volume_name
        self.created_vol_cap_size = cap_size
        self.pv_name = "some-pv-name"

        if volume_name == None:
            self.created_vol_name = "dockerfile"  # or you might consider to take input or generate some random
        if cap_size == None:
            self.created_vol_cap_size = "5"  # in Gi consider to take input

        pv = client.V1PersistentVolume(
            api_version="v1",
            kind="PersistentVolume",
            metadata=client.V1ObjectMeta(name=self.pv_name, labels={"type": "local"}),
            spec=client.V1PersistentVolumeSpec(
                capacity={"storage": f"{self.created_vol_cap_size}Gi"},
                access_modes=["ReadWriteOnce"],
                persistent_volume_reclaim_policy="Retain",
                host_path=client.V1HostPathVolumeSource(path=self.context_dir),
            ),
        )
        try:
            resp = kube_v1.create_persistent_volume(pv)
            print(resp)
            self.pv_flag = True
            print("\nPersistent Volume created successfully.")
        except client.exceptions.ApiException as e:
            print("Exception when creating persistent volume : %s\n" % e)

    def claim_volume(self, volume_name: str=None, cap_size=None):
        self.pvc_name = "some-pvc-claim"
        pvc = client.V1PersistentVolumeClaim(
            api_version="v1",
            kind="PersistentVolumeClaim",
            metadata=client.V1ObjectMeta(name=self.pvc_name),
            spec=client.V1PersistentVolumeClaimSpec(
                access_modes=["ReadWriteOnce"],
                resources=client.V1ResourceRequirements(requests={"storage": "1Gi"}),
            ),
        )
        try:
            resp = kube_v1.create_namespaced_persistent_volume_claim(
                namespace="default", body=pvc
            )
            print(resp)
            self.pvc_flag = True
            print("Persistent Volume Claim created successfully.\n")
        except client.exceptions.ApiException as e:
            print("Exception when creating persistent volume claim : %s\n" % e)

    def create_kube_secret(self):
        # Define your Docker registry credentials
        docker_config_json = {
            "auths": {
                "https://index.docker.io/v1/": {  # Docker Hub URL
                    "username": f"{self.docker_username}",
                    "password": f"{self.docker_pass}",
                    "email": f"{self.docker_email}",
                }
            }
        }
        # Encode the Docker config JSON to base64
        encoded_docker_config = base64.b64encode(
            json.dumps(docker_config_json).encode()
        ).decode()
        # Create a V1Secret object for Docker registry
        secret = client.V1Secret(
            api_version="v1",
            kind="Secret",
            metadata=client.V1ObjectMeta(
                name="docker-registry-secret", namespace="default"
            ),  # Adjust the namespace as needed
            data={".dockerconfigjson": encoded_docker_config},
            type="kubernetes.io/dockerconfigjson",
        )
        try:
            api_response = kube_v1.create_namespaced_secret(
                namespace="default", body=secret
            )
            print("Secret created. Status='%s'\n" % str(api_response))
            print(api_response)
        except client.exceptions.ApiException as e:
            print("Exception when creating secret: %s\n" % e)

        # kube_v1.create_namespaced_secret(namespace='willsee', body=client.V1Secret())
        # subprocess.run(
        #     [
        #         "kubectl",
        #         "create",
        #         "secret",
        #         "docker-registry",
        #         "regcred",
        #         f"--docker-server=https://index.docker.io/v1/",
        #         f"--docker-username={self.docker_username}",
        #         f"--docker-password={self.docker_pass}",
        #         f"--docker-email={self.docker_email}",
        #     ]
        # )

    def create_job(self):
        # Define the Job spec
        self.vol_secret_name = "docker-secret"
        volume_mount_list = [
            client.V1VolumeMount(
                name='docker-registry-secret', mount_path="/kaniko/.docker"
            )
        ]
        volume_list = [
            client.V1Volume(
                name='docker-registry-secret',
                secret=client.V1SecretVolumeSource(
                    secret_name=self.vol_secret_name,
                    items=[
                        client.V1KeyToPath(key=".dockerconfigjson", path="config.json")
                    ],
                ),
            )
        ]
        if self.pvc_flag:
            volume_mount_list.append(
                client.V1VolumeMount(name="dockerfile-storage", mount_path="/workspace")
            )
            volume_list.append(
                client.V1Volume(
                    name="dockerfile-storage",
                    persistent_volume_claim=client.V1PersistentVolumeClaimVolumeSource(
                        claim_name=self.pvc_name
                    ),
                )
            )
        job_spec = client.V1JobSpec(
            template=client.V1JobTemplateSpec(
                # metadata=client.V1ObjectMeta(labels={"app": "job"}),
                spec=client.V1JobSpec(
                    containers=[
                        client.V1Container(
                            name="kaniko",
                            image="gcr.io/kaniko-project/executor:latest",
                            args=[
                                f"--context={self.context_dir}",
                                f"--dockerfile={self.docker_filepath}",
                                f'{"--no-push" if self.no_push else ("--destination="+self.docker_username+'/'+self.docker_repo)}',
                            ],
                            volume_mounts=volume_mount_list,
                        )
                    ],
                    restart_policy="Never".capitalize,
                    volumes=volume_list,
                ),
            ),
            backoff_limit=3,
        )

        # Define the Job object
        job = client.V1Job(
            api_version="batch/v1",
            kind="Job",
            metadata=client.V1ObjectMeta(name="example-job"),
            spec=job_spec,
        )

        # Create the Job in the specified namespace
        api_instance = client.BatchV1Api()
        try:
            api_response = api_instance.create_namespaced_job(
                namespace="default", body=job
            )
            print(f"Job created. Status='{api_response.status}'\n")
        except client.exceptions.ApiException as e:
            print(f"Exception when creating job: {e}\n")

    def create_pod(self):
        self.vol_secret_name = "docker-secret"
        volume_mount_list = [
            client.V1VolumeMount(
                name=self.vol_secret_name, mount_path="/kaniko/.docker"
            )
        ]
        volume_list = [
            client.V1Volume(
                name=self.vol_secret_name,
                secret=client.V1SecretVolumeSource(
                    secret_name='docker-registry-secret',
                    items=[
                        client.V1KeyToPath(key=".dockerconfigjson", path="config.json")
                    ],
                ),
            )
        ]
        if self.pvc_flag:
            volume_mount_list.append(
                client.V1VolumeMount(name="dockerfile-storage", mount_path="/workspace")
            )
            volume_list.append(
                client.V1Volume(
                    name="dockerfile-storage",
                    persistent_volume_claim=client.V1PersistentVolumeClaimVolumeSource(
                        claim_name=self.pvc_name
                    ),
                )
            )
        pod = client.V1Pod(
            api_version="v1",
            kind="Pod",
            metadata=client.V1ObjectMeta(name="kaniko"),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="kaniko",
                        image="gcr.io/kaniko-project/executor:latest",
                        args=[
                            f"--context={self.context_dir}",
                            f"--dockerfile={self.docker_filepath}",
                            f'{"--no-push" if self.no_push else ("--destination="+self.docker_username+'/'+self.docker_repo)}',
                        ],
                        volume_mounts=volume_mount_list,
                    )
                ],
                restart_policy="Never",
                volumes=volume_list,
            )
        )
        
        try:
            api_response = kube_v1.create_namespaced_pod(namespace="default", body=pod)
            print(f"Job created. Status='{api_response.status}'\n")
        except client.exceptions.ApiException as e:
            print(f"Exception when creating job: {e}\n")

@click.command()
@click.argument("cmd")
@click.option("--context_dir", type=str, default=None, help="")
@click.option("--docker_filepath", type=str, default="Dockerfile", help="")
@click.option("--no_push", is_flag=True, default=False, help="")
@click.option("--docker_username", type=str, default=None, help="")
@click.option("--docker_email", type=str, default=None, help="")
@click.option("--docker_repo", type=str, default=None, help="")
def main(
    cmd,
    context_dir,
    docker_filepath,
    no_push,
    docker_username,
    docker_repo,
    docker_email=None,
):
    if cmd not in AVAILABLE_CMDS:
        print("No such commands found.\n")
        return
    if cmd != "deploy":
        return

    if no_push == False:
        if docker_email == None:
            docker_email = input("Enter docker email : ")
        if docker_username == None:
            docker_username = input("Enter docker username : ")
        docker_pass = getpass.getpass("Enter docker password : ")

    kaniko_build = KanikoBuild(
        context_dir,
        docker_filepath,
        no_push,
        docker_username,
        docker_repo,
        docker_pass,
        docker_email=None,
    )

    if Path(KANIKO_BUILD_FILENAE).exists():
        Path(KANIKO_BUILD_FILENAE).unlink()

    kaniko_build.build()
    pod_lists = kube_v1.list_pod_for_all_namespaces(watch=False)
    for pod in pod_lists.items:
        print(f"{pod.status.pod_ip}\t{pod.metadata.namespace}\t{pod.metadata.name}")


if __name__ == "__main__":
    main()

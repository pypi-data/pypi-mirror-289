
##README.md

This tool can be used to create and push a docker image from local or open remote directory to docker hub(can be private).
For local directories, tool will create a persistent-volume, persitent-volume-claim, and kaniko-pod temporary and all will be deleted once the image has been pushed to the docker hub.

#Installation
pip install kaniko_deploy

Make sure to have connection with kubernetes.
*for remote kubenetes obtain kubernetes config file and set it's path to env var KUBECONFIG ,(else keep it at respective OS ~/.kube/config path)

if using minikube, and getting dockerfile not found error, then first mount usinng `minikube mount $WORKDIR:/<your-kube-work-dir>`

Steps :
    1. For local directories open the terminal wherever your project is (anywhere for remote directories)
    2. either create python3.12 virtual env and then install the kaniko_build(recommended) or can be installed globally also 
    3. it is recommended to create volume.yaml, volume-claim.yaml (once for each project) so to provide configs as user's requirements or wish
    4. run the below mentioned example command

replace the username, email and docker repo with yours (if docker secrets not present then password will be asked for first time)

#Exmaple command 
python -m kaniko_deploy deploy --context_dir=git://github.com//Imoustak/kaniko-build-demo.git --docker_filepath=dockerfile --docker_username=<your-docker-username> --docker_email=<your-docker-email> --docker_repo=<your-repo>


Note:
Currently this is desgined for namespace default only, can be further editted to handle dynamic namespaces
Secret name for docker-registry is considered as "docker-registry-secret",



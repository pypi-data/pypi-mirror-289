from setuptools import setup, find_packages
import kaniko_deploy

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith("#")]

setup(
    name=kaniko_deploy.__title__,
    version='0.2',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    python_requires='>=3.12',
    entry_points={
        'console_scripts': [
            'kaniko_deploy=kaniko_deploy.main:main',  # Replace with your main entry point
        ],
    },
    license='MIT'
    # Include other metadata as needed
)
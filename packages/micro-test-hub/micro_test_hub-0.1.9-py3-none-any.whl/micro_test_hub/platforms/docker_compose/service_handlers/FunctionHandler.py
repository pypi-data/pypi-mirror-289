import tempfile
from micro_test_hub.services.Service import Service
import os
import random
import textwrap
import copy
import git

class FunctionHandler(): 

    default_conf = {
                        "platform": "linux/amd64",
                            "healthcheck": 
                            {
                                "test": [
                                    "CMD-SHELL", "sh", "-c", "nc -z 127.0.0.1 8080 || exit 1"
                                ],"interval": "5s",
                                "timeout": "2s",
                                "retries": 3,
                                "start_period": "1s"
                            },
                            "build": {
                                            "context": "{code_folder}",
                                            "dockerfile": "dockerfile.docker"
                                            },
                            "ports": "{host_port}:8080"
                        }
    
    
    
    @classmethod
    def _create_docker_file(cls, code_folder, docker_file_content):
       os.makedirs(code_folder, exist_ok=True)
       docker_file_content = docker_file_content.replace("{code_folder}", code_folder) 
       docker_file_content = textwrap.dedent(docker_file_content)  # Remove leading spaces
       with open(f"{code_folder}/dockerfile.docker", "w") as file:
            file.write(docker_file_content)    
            file_path = file.name
       os.chmod(file_path, 0o755)  # Set executable permissions
       return file_path    

            
                                
    @classmethod
    def _load_default_config(cls, host_port_index, code_folder, temp_sh_file):
        host_port = str(6000 + host_port_index)
        # get filename from file path
        config = copy.deepcopy(cls.default_conf)
        config['ports'] = [config['ports'].replace("{host_port}", host_port)]
        config['build']['context'] = code_folder
            
        return config
    
    
    @classmethod        
    def _common_build(cls, service: Service, index: int, code_folder: str, docker_file_path: str):     
        service_dict = {}
         
        service_dict = cls._load_default_config(index, code_folder, docker_file_path)    
        service_dict['environment'] = service.env_vars
        if service.depends_on_services:
            depends_on = {}
            env_update = {}
            for dependency in service.depends_on_services:
                depends_on.update({
                                    dependency.name : {
                                        "condition": "service_healthy"
                                    }
                                    })
                if dependency.type == 'GCP' and dependency.service_type == 'FIRESTORE':
                    env_update.update({
                        "FIRESTORE_EMULATOR_HOST": f"{dependency.name}:8080"
                    })
                elif dependency.type == 'GCP' and dependency.service_type == 'PUBSUB':
                    env_update.update({
                        "PUBSUB_EMULATOR_HOST": f"{dependency.name}:8085"
                    })
                elif dependency.type == 'GCP' and dependency.service_type == 'STORAGE':
                    env_update.update({
                        "STORAGE_EMULATOR_HOST": "http://gcs_storage_proxy:5050"
                    })        
            service_dict["depends_on"] = depends_on
            service_dict["environment"].update(env_update)
        return service_dict         


class NodeFunctionHandler(FunctionHandler):                
    
    docker_file_content = """
# Use the official lightweight Node.js 14 image.
# https://hub.docker.com/_/node
FROM node:14-slim

# Create and change to the app directory.
WORKDIR /usr/src/app

# Copy application dependency manifests to the container image.
# A wildcard is used to ensure both package.json AND package-lock.json are copied.
# Copying this separately prevents re-running npm install on every code change.
COPY ./package*.json ./

# Install production dependencies.
RUN npm install --only=production

# Install Functions Framework
RUN npm install @google-cloud/functions-framework

# Copy local code to the container image.
COPY . .

# Use the Functions Framework to serve the function.
CMD ["npx", "functions-framework", "--target=main"]
"""

   
    @classmethod        
    def build(cls, service: Service, index: int):     
        service_dict = {}
        
        random_number = random.randint(1000, 9999)
        temp_dir = tempfile.gettempdir()
        code_repo_folder = f"/tmp/{service.name}_{random_number}"
        if service.code_folder:
            code_folder = f"{code_repo_folder}/{service.code_folder}"
        else:
            code_folder = code_repo_folder    
        # git clone the code repo
        git.Repo.clone_from(service.code_repo, code_repo_folder, branch=service.code_branch)
        docker_file_path = cls._create_docker_file(code_folder, cls.docker_file_content)    
        service_dict = cls._common_build(service, index, code_folder, docker_file_path)
        
        return service_dict  

    
    
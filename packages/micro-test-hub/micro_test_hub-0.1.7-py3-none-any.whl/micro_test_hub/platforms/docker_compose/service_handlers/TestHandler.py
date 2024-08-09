import tempfile
from typing import List
from micro_test_hub.services.Service import Service
import os
import random
import textwrap
import copy
import shutil

class TestHandler(): 

    default_conf = {
                        "platform": "linux/amd64",
                            "build": {
                                            "context": "{code_folder}",
                                            "dockerfile": "dockerfile.docker"
                                            },
                            "depends_on": {}
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
    def _load_default_config(cls, code_folder, temp_sh_file):
        # get filename from file path
        config = copy.deepcopy(cls.default_conf)
        config['build']['context'] = code_folder
            
        return config
    
    
    @classmethod        
    def _common_build(cls, dependencies: List, code_folder: str, docker_file_path: str):     
        service_dict = {}
        depends_on = {} 
        service_dict = cls._load_default_config(code_folder, docker_file_path)    
        for dependency in dependencies:
                depends_on.update({
                                    dependency : {
                                        "condition": "service_healthy"
                                    }
                                    })
        service_dict["depends_on"] = depends_on
        return service_dict         

    @classmethod
    def _get_dependencies(cls, services: List[Service]):
        dependencies = []
        for service in services:
            if service.downstream:
                dependencies.append(service.name)
        #dependencies.append("pub_sub_initiator")     
        return dependencies
    
class PythonTestHandler(TestHandler):                
    
    docker_file_content = """
FROM --platform=linux/amd64 python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./* /app
CMD ["python3", "main.py"]
"""

   
    @classmethod        
    def build(cls, project_name, services: List[Service], test_path: str):     
        service_dict = {}
        
        random_number = random.randint(1000, 9999)
        temp_dir = tempfile.gettempdir()
        test_folder = f"/{temp_dir}/{project_name}_tests_{random_number}"
        # copy the contest of the tests_path to the test_folder
        shutil.copytree(test_path, test_folder, dirs_exist_ok=True)
                
        docker_file_path = cls._create_docker_file(test_folder, cls.docker_file_content)  
        dependencies = cls._get_dependencies(services)  
        service_dict = cls._common_build(dependencies, test_folder, docker_file_path)
        
        return service_dict  

    
    
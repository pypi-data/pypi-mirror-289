import tempfile
from micro_test_hub.services.Service import Service
import os
import random
import copy
import shutil


class StorageHandler(): 

    default_conf = {
                    "platform": "linux/amd64",
                        "healthcheck": 
                        {
                            "test": [
                                "CMD-SHELL", "sh", "-c", "nc -z 127.0.0.1 4443 || exit 1"
                            ],"interval": "5s",
                            "timeout": "2s",
                            "retries": 3,
                            "start_period": "1s"
                        },
                        "environment": {
                            "PORT": "4443",
                            "DATA": "/data"
                        },
                        "image": "fsouza/fake-gcs-server",
                        "ports": "{host_port}:4443",
                        "volumes": ["{storage_folder}:/data"]

                    }
    
                                   
    @classmethod
    def _load_default_config(cls, host_port_index, storage_folder):
        host_port = str(4443 + host_port_index)
        # get filename from file path
        config = copy.deepcopy(cls.default_conf)
        config['ports'] = [config['ports'].replace("{host_port}", host_port)]
        for index, volume in enumerate(config['volumes']):
            config['volumes'][index] = config['volumes'][index].replace("{storage_folder}", storage_folder)
            
        return config
    
    @classmethod
    def _create_empty_file(cls, file_path):
        with open(file_path, "w") as file:
            file.write("")
        return file_path
    
    @classmethod        
    def build(cls, service:Service, index: int):     
        random_number = random.randint(1000, 9999)
        temp_dir = tempfile.gettempdir()
        storage_folder = f"/{temp_dir}/{service.name}_{random_number}"
        os.makedirs(storage_folder, exist_ok=True)
        for bucket in service.buckets:
            os.makedirs(f"{storage_folder}/{bucket.name}", exist_ok=True)
            if bucket.location:
                # copy the content of the bucket.location to the bucket folder
                shutil.copytree(bucket.location, f"{storage_folder}/{bucket.name}", 
                                                            dirs_exist_ok=True)
            else:
                # create an empty file in the bucket folder
                cls._create_empty_file(f"{storage_folder}/{bucket.name}/empty_file")                          
            
        return cls._load_default_config(index, storage_folder)             

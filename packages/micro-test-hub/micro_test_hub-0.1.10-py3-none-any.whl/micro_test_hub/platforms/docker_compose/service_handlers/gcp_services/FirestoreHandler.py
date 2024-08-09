import copy


class FirestoreHandler(): 

    default_conf = {
                        "platform": "linux/amd64",
                        "image": "google/cloud-sdk",
                        "healthcheck": 
                        {
                            "test": [
                                "CMD-SHELL", "sh", "-c", "nc -z 127.0.0.1 8080 || exit 1"
                            ],"interval": "5s",
                            "timeout": "2s",
                            "retries": 3,
                            "start_period": "1s"
                        },
                        "environment": {
                            "CLOUDSDK_CORE_PROJECT": "your-project-id"
                        },
                        "ports": "{host_port}:8080",
                        "command": "gcloud beta emulators firestore start --host-port=0.0.0.0:8080"
                        }
    
                                   
    @classmethod
    def _load_default_config(cls, host_port_index):
        host_port = str(8090 + host_port_index)
        # get filename from file path
        config = copy.deepcopy(cls.default_conf)
        config['ports'] = [config['ports'].replace("{host_port}", host_port)]
            
        return config
    
    
    @classmethod        
    def build(cls, index: int):     
        return cls._load_default_config(index)             
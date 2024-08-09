from micro_test_hub.services.Service import Service


class DockerHandler(): #pragma: no cover

    @classmethod        
    def build(cls, service: Service):     
        service_dict = {}
        if service.platform:
            service_dict["platform"] = service.platform    
        if service.env_vars:
            service_dict["environment"] = service.env_vars    
        if service.container_command:
            service_dict["command"] = service.container_command
        if service.container_command_args:
            service_dict["command_args"] = service.container_command_args        
        if service.volumes:
            volumes = []
            for volume in service.volumes:
                volumes.append(f"{volume['host']}:{volume['container']}")
            service_dict["volumes"] = volumes
        if service.host_port and service.container_port:
            service_dict["ports"] = [f"{service.host_port}:{service.container_port}"]
            service_dict["healthcheck"] = {
                                                                
                                                                    "test": [
                                                                    "CMD-SHELL",
                                                                    "sh",
                                                                    "-c",
                                                                    f"nc -z 127.0.0.1 {service.container_port} || exit 1"
                                                                    ],
                                                                    "interval": "5s",
                                                                    "timeout": "2s",
                                                                    "retries": 3,
                                                                    "start_period": "1s"
                                                                }
            
        else:
            raise ValueError("Host port and container port are required for Docker services.")
        if service.image_uri:
            service_dict["image"] = service.image_uri
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
    
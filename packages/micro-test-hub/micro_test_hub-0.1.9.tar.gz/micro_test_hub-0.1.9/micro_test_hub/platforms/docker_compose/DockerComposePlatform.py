import yaml
from typing import List, Optional
import subprocess
from pydantic import BaseModel
from micro_test_hub.platforms.IPlatform import IPlatform
from micro_test_hub.platforms.docker_compose.service_handlers.FunctionHandler import NodeFunctionHandler
from micro_test_hub.platforms.docker_compose.service_handlers.gcp_services.FirestoreHandler import FirestoreHandler
from micro_test_hub.platforms.docker_compose.service_handlers.gcp_services.PubSubHandler import PubSubHandler
from micro_test_hub.platforms.docker_compose.service_handlers.gcp_services.StorageHandler import StorageHandler
from micro_test_hub.platforms.docker_compose.service_handlers.gcp_services.StorageProxy import StorageProxy
from micro_test_hub.platforms.docker_compose.service_handlers.PostgresHandler import PostgresHandler
from micro_test_hub.platforms.docker_compose.service_handlers.TestHandler import PythonTestHandler
from micro_test_hub.services.Service import Service
from micro_test_hub.platforms.docker_compose.service_handlers.DockerHandler import DockerHandler

class DockerComposePlatform(BaseModel, IPlatform): #pragma: no cover

    yaml_input: Optional[str] = None
    test_results: Optional[bool] = None
    
    def validate_yaml_input(self) -> bool:
        try:
            yaml.safe_load(self.yaml_input)
            return True  # The YAML is valid
        except yaml.YAMLError as e:
            print(f"Invalid YAML string: {e}")
            return False  # The YAML is invalid
            
    def build(self, services: List[Service], tests_path: str, project_name: str):     
        data = {
            "version": "3",
            "services": {},
        }
        for index, service in enumerate(services):
            data["services"][service.name] = {}
            if service.type == "DOCKER":
                data["services"][service.name] = DockerHandler.build(service)
            elif service.type == "DB" and service.db_type == "POSTGRESS":
                data["services"][service.name] = PostgresHandler.build(service, index)
            elif service.type == "FUNCTION" and service.lang_type == "NODEJS":
                data["services"][service.name] = NodeFunctionHandler.build(service, index)
            elif service.type == "GCP" and service.service_type == "FIRESTORE":
                data["services"][service.name] = FirestoreHandler.build(index)
            elif service.type == "GCP" and service.service_type == "STORAGE":
                data["services"][service.name] = StorageHandler.build(service, index)
                data["services"]["gcs_storage_proxy"] = StorageProxy.build(service, index)
            elif service.type == "GCP" and service.service_type == "PUBSUB":
                data["services"][service.name] = PubSubHandler.build(project_name, service, index)             
                data["services"]["pub_sub_initiator"] = PubSubHandler.build_initiator(project_name, service, index)
                #pass
            else:    
                raise ValueError("Service type not supported")
        if tests_path:
            data["services"]["tests"] = PythonTestHandler.build(project_name, services, tests_path)    
        self.yaml_input = yaml.dump(data)
        #print(f"{self.yaml_input}") 
               
                            
    def run(self, mode: str):
        
        if not self.validate_yaml_input():
            print("YAML validation failed. Aborting operation.")
            return
        
        try:
            if mode == 'detached':
                # Start a subprocess that runs docker-compose with stdin as the input
                process = subprocess.Popen(['docker', 'compose', '-f', '-', 'up', '--build', '-d'], stdin=subprocess.PIPE, text=True)
            else:
                # Start a subprocess that runs docker-compose with stdin as the input
                process = subprocess.Popen(['docker', 'compose', '-f', '-', 'up', '--build'], stdin=subprocess.PIPE, text=True)
            # Write the YAML string to docker-compose's stdin
            process.communicate(input=self.yaml_input)
            if process.returncode == 0:
                print("Docker Compose up executed successfully.")
            else:
                print(f"Failed to run Docker Compose up with return code {process.returncode}")
            
            logs_process = subprocess.Popen(['docker', 'compose', '-f', '-', 'logs', '-f', 'tests'], stdin=subprocess.PIPE,stdout=subprocess.PIPE, text=True)
            
            #time.sleep(5)  # Give it a moment to terminate
            # Write the YAML string to docker-compose's stdin
            stdout, _ = logs_process.communicate(input=self.yaml_input)
            if logs_process.returncode == 0:
                print("Docker Compose logs executed successfully.")
            else:
                print(f"Failed to run Docker Compose logs with return code {logs_process.returncode}")
            exit_code = None
            # Parse the output for service exit codes
           
            if stdout:
                for line in stdout.splitlines():
                    if "exited with code" in line:
                        exit_code = line.split("exited with code")[1].strip()
                        break
            else:
                print("Stdout is empty.")
            print(f"{stdout}")
    
            if exit_code in ["0"]:
                self.test_results = True
            else:
                self.test_results = False

            # Stop the subprocess
            logs_process.terminate()  # Try to terminate the process gently

            # Optionally, wait a bit to see if the process terminates gracefully
            #time.sleep(2)  # Give it a moment to terminate

            if logs_process.poll() is None:  # Check if the process has indeed terminated
                print("Process did not terminate, killing it.")
                logs_process.kill()  # Forcefully kill the process if it didn't terminate
            else:
                print("Process terminated successfully.")                
        except Exception as e:
            print(f"An error occurred: {e}")
        

    def shutdown_services(self):
        try:
            # Execute docker compose down command
            result = subprocess.run(['docker', 'compose', '-f', '-', 'down'], input=self.yaml_input, text=True, capture_output=True)
            
            if result.returncode == 0:
                print("Successfully shut down all services.")
            else:
                print(f"Failed to shut down services with return code {result.returncode}. Error: {result.stderr}")
        except Exception as e:
            print(f"An error occurred while trying to shut down services: {e}")
                
    def get_test_results(self) -> bool:
        return self.test_results        

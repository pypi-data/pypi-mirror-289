from time import time
import yaml
from typing import List, Optional
import subprocess
from pydantic import BaseModel
from platforms.IPlatform import IPlatform
from services.Service import Service
import os

class DCPlatform(BaseModel, IPlatform): #pragma: no cover

    yaml_input: Optional[str] = None
    test_results: Optional[bool] = None
    
    def validate_yaml_input(self) -> bool:
        try:
            yaml.safe_load(self.yaml_input)
            return True  # The YAML is valid
        except yaml.YAMLError as e:
            print(f"Invalid YAML string: {e}")
            return False  # The YAML is invalid
        
    def build(self, services: List[Service], tests_path: str):
        print(f"Current working directory: {os.getcwd()}")
        data = {
            "version": "3",
            "services": {},
            # "networks": {
            #     "simple_feature_management_network": {
            #         "external": True
            #     }
            # }
        }
        depends_on_list = {}
        for service in services:
            if service.downstream:
                depends_on_list.update({
                                        service.name: 
                                            {
                                                "condition": "service_healthy"
                                            }
                                        })
            data["services"][service.name] = {
                "volumes": service.volumes
            }
            if service.platform:
                data["services"][service.name]["platform"] = service.platform
            if service.build:
                data["services"][service.name]["build"] = service.build
            if service.ports:
                data["services"][service.name]["ports"] = [service.ports]
            if service.environment:
                data["services"][service.name]["environment"] = service.environment
            if service.image_uri:
                data["services"][service.name]["image"] = service.image_uri
            if service.depends_on:
                data["services"][service.name]["depends_on"] = service.depends_on
            if service.health_check:
                data["services"][service.name]["healthcheck"] = service.health_check    
            if service.command:
                data["services"][service.name]["command"] = service.command    
        if tests_path:
            data["services"]["tests"] = {
                "build": {
                    "context": f"{tests_path}",
                    "dockerfile": "dockerfile.docker"
                    },
                "depends_on": depends_on_list
            }    
        self.yaml_input = yaml.dump(data)
        print(f"{self.yaml_input}")
        
    def run(self):
        
        if not self.validate_yaml_input():
            print("YAML validation failed. Aborting operation.")
            return
        
        try:
            # Start a subprocess that runs docker-compose with stdin as the input
            process = subprocess.Popen(['docker', 'compose', '-f', '-', 'up', '--build'], stdin=subprocess.PIPE, text=True)
            # Write the YAML string to docker-compose's stdin
            process.communicate(input=self.yaml_input)
            if process.returncode == 0:
                print("Docker Compose up executed successfully.")
            else:
                print(f"Failed to run Docker Compose up with return code {process.returncode}")
            
            logs_process = subprocess.Popen(['docker', 'compose', 'logs', '-f', 'tests'], stdout=subprocess.PIPE, text=True)
            
            #time.sleep(5)  # Give it a moment to terminate
            # Write the YAML string to docker-compose's stdin
            stdout, _ = logs_process.communicate()
            if logs_process.returncode == 0:
                print("Docker Compose up executed successfully.")
            else:
                print(f"Failed to run Docker Compose up with return code {logs_process.returncode}")
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

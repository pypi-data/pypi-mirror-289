import tempfile
import textwrap
from micro_test_hub.services.Service import Service
import os
import random
import copy
import json

class StorageProxy(): 
    
    pub_sub_init_config = { 
                            "platform": "linux/amd64",
                            "build": {
                                            "context": "{code_folder}",
                                            "dockerfile": "dockerfile.docker"
                                            },
                            "environment": {
                                                "NODE_TLS_REJECT_UNAUTHORIZED":"0"
                                            },
                            "depends_on": "{gcs_emulator_host}",
                            "ports": "{host_port}:5050",
                            }
    
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

# Copy local code to the container image.
COPY . .

# Run the web service on container startup.
CMD ["node", "index.js"]
"""

    init_script_content = """const http = require('http');
const httpProxy = require('http-proxy');

// Create a proxy server with custom application logic
const proxy = httpProxy.createProxyServer({
  secure: false // Disable SSL verification
});

const server = http.createServer(function(req, res) {
  // Check if the request method is GET and the URL does not already include /storage/v1
  if (req.method === 'GET' && !req.url.startsWith('/storage/v1')) {
    req.url = '/storage/v1' + req.url; // Prepend /storage/v1 to the URL for GET requests
  }

  // Proxy the request to the GCS emulator
  proxy.web(req, res, { target: 'https://##gcs_emulator##:4443' });
});

console.log("Listening on port 5050")
server.listen(5050);     
"""

    package_json ={
    "name": "http_proxy",
    "version": "1.0.0",
    "description": "A simple Node.js app running in Docker",
    "main": "index.js",
    "scripts": {
      "start": "node index.js"
    },
    "dependencies": {
      "http-proxy": "^1.18.1"
    }
  }
                                   
    @classmethod
    def _load_config(cls, host_port_index, service_name, service_folder):
        host_port = str(5050 + host_port_index)
        # get filename from file path
        config = copy.deepcopy(cls.pub_sub_init_config)
        config['ports'] = [config['ports'].replace("{host_port}", host_port)]
        config['depends_on'] = [config['depends_on'].replace("{gcs_emulator_host}", service_name)]
        config['build']['context'] = service_folder
        
        return config
    
    @classmethod
    def _create_init_file(cls, service_name, service_folder, init_file_content):
       init_file_content = textwrap.dedent(init_file_content)  # Remove leading spaces
       init_file_content = init_file_content.replace("##gcs_emulator##", service_name) 
       os.makedirs(service_folder, exist_ok=True)
       with open(f"{service_folder}/index.js", "w") as file:
            file.write(init_file_content)    
            file_path = file.name
       os.chmod(file_path, 0o755)  # Set executable permissions
       return file_path    
   
    @classmethod
    def _create_docker_file(cls, service_folder, docker_file_content):
       os.makedirs(service_folder, exist_ok=True)
       os.makedirs(service_folder, exist_ok=True)
       docker_file_content = textwrap.dedent(docker_file_content)  # Remove leading spaces
       with open(f"{service_folder}/dockerfile.docker", "w") as file:
            file.write(docker_file_content)    
            file_path = file.name
       os.chmod(file_path, 0o755)  # Set executable permissions
       return file_path 

    
    @classmethod
    def create_package_json(cls, service_folder):
        with open(f"{service_folder}/package.json", "w") as file:
            file.write(json.dumps(cls.package_json))    
            file_path = file.name
        return file_path
       
    
    @classmethod        
    def build(cls, service:Service, index: int):     
        random_number = random.randint(1000, 9999)
        temp_dir = tempfile.gettempdir()
        service_folder = f"/{temp_dir}/{service.name}_proxy_{random_number}"                         
        cls._create_init_file(service.name, service_folder, cls.init_script_content)            
        cls._create_docker_file(service_folder, cls.docker_file_content)
        cls.create_package_json(service_folder)
        return cls._load_config(index, service.name, service_folder)             


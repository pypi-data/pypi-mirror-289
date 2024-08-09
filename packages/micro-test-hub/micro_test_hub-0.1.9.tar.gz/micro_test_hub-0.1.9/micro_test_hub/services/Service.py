from typing import Dict, List, Optional

from pydantic import BaseModel
from enum import Enum

class GCPServiceType(str, Enum):
    FIRESTORE = 'FIRESTORE'
    PUBSUB = 'PUBSUB'
    STORAGE = 'STORAGE'

class ServiceType(str, Enum):
    DOCKER = 'DOCKER'
    GCP = 'GCP'
    FUNCTION = 'FUNCTION'
    DB = 'DB'    

class DBType(str, Enum):
    POSTGRESS = 'POSTGRESS'
                
class LANGType(str, Enum):
    NODEJS = 'NODEJS'
    PYTHON = 'PYTHON'

class GCPSubscription(BaseModel):
    name: str
    push_endpoint: str

class GCPTopic(BaseModel):
    name: str
    subscriptions: List[GCPSubscription]

class GCPBucket(BaseModel):
    name: str
    location: Optional[str] = None
    
class Service(BaseModel):
    id: Optional[str] = None
    name: str
    type: ServiceType
    downstream: bool
    platform: Optional[str] = "linux/amd64" # Default value for non linux platforms
    env_vars: Optional[Dict[str, str | int]] = None
    volumes: Optional[List[Dict[str, str]]] = None
    container_command: Optional[str] = None
    container_command_args: Optional[str] = None
    dependencies: Optional[List[str]] = None

class DockerService(Service):
    image_uri: str
    container_port: int
    host_port: int
    depends_on_services: Optional[List[Service]] = None
        
class GCPService(Service):
    service_type: GCPServiceType
    container_port: Optional[int] = None
    host_port: Optional[int] = None
    depends_on_services: Optional[List[Service]] = None

class GCPStorageService(GCPService):
    buckets: List[GCPBucket]
    
class GCPPubSubService(GCPService):
    topics: List[GCPTopic]
    
class FunctionService(Service):
    code_repo: str
    code_branch: str
    code_folder: Optional[str] = None
    lang_type: LANGType
    container_port: Optional[int] = None
    host_port: Optional[int] = None
    depends_on_services: Optional[List[Service]] = None

class DBService(Service):
    db_type: DBType
    container_port: Optional[int] = None
    host_port: Optional[int] = None
    sql_init_file: Optional[str] = None
    depends_on_services: Optional[List[Service]] = None
    
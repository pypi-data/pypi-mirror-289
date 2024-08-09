from typing import Dict, List, Optional
from micro_test_hub.platforms.IPlatform import IPlatform
from pydantic import BaseModel
from micro_test_hub.platforms.docker_compose.DockerComposePlatform import DockerComposePlatform
from micro_test_hub.services.Service import DBService, DockerService, FunctionService, GCPPubSubService, GCPService, GCPStorageService, Service, ServiceType
from micro_test_hub.test_suites.MicroTestSuite import MicroTestSuite
from enum import Enum

class PlatformType(str, Enum):
    DOCKER = 'DOCKER-COMPOSE'
    GCP = 'GCP'
    
    
class MicroTestProject(BaseModel):
    name: str
    platform: PlatformType
    micro_test_suite: Optional[MicroTestSuite]=None
    tests_path: str
    services: List[Dict]
    
    def _build_services(self):
        services = []
        
        for service in self.services:
            if service['type'] == ServiceType.DOCKER:
                service = DockerService(**service)
            elif service['type'] == 'GCP' and service['service_type'] == 'STORAGE':
                    service = GCPStorageService(**service)
            elif service['type'] == 'GCP' and service['service_type'] == 'FIRESTORE':    
                    service = GCPService(**service)
            elif service['type'] == 'GCP' and service['service_type'] == 'PUBSUB':    
                    service = GCPPubSubService(**service)
            elif service['type'] == 'FUNCTION':
                service = FunctionService(**service)    
            elif service['type'] == 'DB':
                service = DBService(**service)    
            else:
                raise ValueError("Service type not supported")
            services.append(service)
        return services        
    
    def _build_platform(self):
        if self.platform == PlatformType.DOCKER:
            return DockerComposePlatform()
        elif self.platform == PlatformType.GCP:
            pass
        else:
            raise ValueError("Platform not supported")
        
    def run_test(self, mode: str):        
        test_suite = MicroTestSuite(id="1", name=self.name, 
                                    services=self._build_services(), 
                                    platform=self._build_platform(), 
                                    tests_path=self.tests_path)
        test_suite.run(mode)
        results = test_suite.test_results()
        test_suite.stop()
        return results
from typing import Dict, List, Optional
from micro_test_hub.platforms.IPlatform import IPlatform
from pydantic import BaseModel
from micro_test_hub.services.Service import Service


class MicroTestSuite(BaseModel):
    id: Optional[str]
    name: str
    services: List[Service]
    platform: IPlatform
    tests_path: str

    def _find_service_by_name(self, name):
        for service in self.services:
            if service.name == name:
                return service
        return None
    
    def _set_depends_on_services(self):
        for service in self.services:
            if service.dependencies and hasattr(service, 'depends_on_services'):
                service.depends_on_services = [self._find_service_by_name(dep) for dep in service.dependencies]
                                    
    def run(self, mode: str):
        self._set_depends_on_services()
        self.platform.build(self.services, self.tests_path, self.name)
        self.platform.run(mode)
    
    def stop(self):
        self.platform.shutdown_services()
        
    def test_results(self):
        return self.platform.get_test_results()    
        
    class Config:
        arbitrary_types_allowed = True    
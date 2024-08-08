from abc import ABC, abstractmethod
from typing import List
from services.Service import Service

class IPlatform(ABC): #pragma: no cover

    @abstractmethod
    def build(self, services: List[Service]):
        pass

    @abstractmethod
    def run(self):
        pass

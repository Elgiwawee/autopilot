# cloud/control_planes/base.py
from abc import ABC, abstractmethod

class ControlPlane(ABC):

    @abstractmethod
    def fetch_workloads(self):
        pass

    @abstractmethod
    def fetch_metrics(self):
        pass

    @abstractmethod
    def execute_action(self, action):
        pass

    @abstractmethod
    def rollback(self, action):
        pass

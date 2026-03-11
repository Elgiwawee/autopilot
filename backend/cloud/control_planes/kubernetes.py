# cloud/control_planes/kubernetes.py
from cloud.control_planes.base import ControlPlane


class KubernetesControlPlane(ControlPlane):
    def execute_action(self, action):
        action.execute(self)

    def rollback(self, action):
        action.rollback(self)

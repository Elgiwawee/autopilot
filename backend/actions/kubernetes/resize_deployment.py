# actions/kubernetes/resize_deployment.py
from kubernetes import client

class ResizeDeploymentAction:

    type = "resize"

    def execute(self, control_plane):
        apps = client.AppsV1Api()

        apps.patch_namespaced_deployment(
            name=self.deployment,
            namespace=self.namespace,
            body=self.new_spec
        )

    def rollback(self, control_plane):
        apps = client.AppsV1Api()

        apps.patch_namespaced_deployment(
            name=self.deployment,
            namespace=self.namespace,
            body=self.previous_spec
        )

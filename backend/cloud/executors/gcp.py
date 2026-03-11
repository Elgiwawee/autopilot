# cloud/executors/gcp.py

from cloud.executors.base import CloudExecutor
from cloud.providers.gcp import GCPProvider


class GCPExecutor(CloudExecutor):
    """
    Executes actions on GCP resources.
    Focus: GKE, Compute Engine, batch workloads.
    """

    def __init__(self, cloud_account):
        super().__init__(cloud_account)
        self.provider = GCPProvider(cloud_account)

    def execute(
        self,
        *,
        target_type,
        namespace,
        target_name,
        action,
        parameters,
    ):
        if action == "scale_deployment":
            self._scale_gke_deployment(
                namespace=namespace,
                name=target_name,
                replicas=parameters.get("replicas"),
            )

        elif action == "stop_instance":
            self._stop_compute_instance(
                instance_id=target_name,
                zone=parameters.get("zone"),
            )

        else:
            raise ValueError(f"Unsupported GCP action: {action}")

    # ---------- ACTION IMPLEMENTATIONS ----------

    def _scale_gke_deployment(self, namespace, name, replicas):
        """
        Hook for Kubernetes API / kubectl.
        """
        if replicas is None:
            raise ValueError("replicas parameter required")

        # Real implementation goes here:
        # kubernetes.client.AppsV1Api().patch_namespaced_deployment_scale(...)
        pass

    def _stop_compute_instance(self, instance_id, zone):
        """
        Stop GCE VM.
        """
        # compute_v1.InstancesClient().stop(...)
        pass

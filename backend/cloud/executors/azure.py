# cloud/executors/azure.py

from cloud.executors.base import CloudExecutor
from cloud.providers.azure import AzureProvider


class AzureExecutor(CloudExecutor):
    """
    Executes actions on Azure resources.
    Focus: AKS, VM scale sets, compute optimization.
    """

    def __init__(self, cloud_account):
        super().__init__(cloud_account)
        self.provider = AzureProvider(cloud_account)

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
            self._scale_aks_deployment(
                namespace=namespace,
                name=target_name,
                replicas=parameters.get("replicas"),
            )

        elif action == "stop_vm":
            self._stop_virtual_machine(
                vm_id=target_name,
                resource_group=parameters.get("resource_group"),
            )

        else:
            raise ValueError(f"Unsupported Azure action: {action}")

    # ---------- ACTION IMPLEMENTATIONS ----------

    def _scale_aks_deployment(self, namespace, name, replicas):
        """
        Hook for AKS Kubernetes scaling.
        """
        if replicas is None:
            raise ValueError("replicas parameter required")

        # Kubernetes API / kubectl / ARM integration here
        pass

    def _stop_virtual_machine(self, vm_id, resource_group):
        """
        Stop Azure VM.
        """
        if not resource_group:
            raise ValueError("resource_group parameter required")

        # ComputeManagementClient.virtual_machines.begin_power_off(...)
        pass

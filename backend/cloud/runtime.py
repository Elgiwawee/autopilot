# cloud/runtime.py

from cloud.providers.aws import AWSProvider
from cloud.providers.gcp import GCPProvider
from cloud.providers.azure import AzureProvider
from cloud.control_planes.kubernetes import KubernetesControlPlane


def get_runtime_handler(account_or_cluster):
    provider = account_or_cluster.provider.name

    if provider == "aws":
        return AWSProvider(account_or_cluster)

    if provider == "gcp":
        return GCPProvider(account_or_cluster)

    if provider == "azure":
        return AzureProvider(account_or_cluster)

    if provider == "kubernetes":
        return KubernetesControlPlane(account_or_cluster)

    raise ValueError(f"Unsupported provider: {provider}")

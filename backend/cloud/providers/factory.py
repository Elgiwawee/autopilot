# cloud/providers/factory.py

from cloud.providers.aws import AWSProvider
from cloud.providers.gcp import GCPProvider
from cloud.providers.azure import AzureProvider

PROVIDERS = {
    "aws": AWSProvider,
    "gcp": GCPProvider,
    "azure": AzureProvider,
}


def get_provider(cloud_account):
    provider_cls = PROVIDERS.get(cloud_account.provider)

    if not provider_cls:
        raise ValueError(
            f"Unsupported cloud provider: {cloud_account.provider}"
        )

    return provider_cls(cloud_account)

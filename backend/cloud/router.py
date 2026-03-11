from cloud.providers.aws import AWSProvider
from cloud.providers.gcp import GCPProvider
from cloud.providers.azure import AzureProvider

def get_provider(account):
    if account.provider == "aws":
        return AWSProvider(account)
    if account.provider == "gcp":
        return GCPProvider(account)
    return AzureProvider(account)

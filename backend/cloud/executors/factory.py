# cloud/executors/factory.py

from cloud.executors.aws import AWSExecutor
from cloud.executors.gcp import GCPExecutor
from cloud.executors.azure import AzureExecutor


EXECUTORS = {
    "aws": AWSExecutor,
    "gcp": GCPExecutor,
    "azure": AzureExecutor,
}


def get_cloud_executor(cloud_account):
    executor_cls = EXECUTORS.get(cloud_account.provider)

    if not executor_cls:
        raise ValueError(
            f"No executor for provider: {cloud_account.provider}"
        )

    return executor_cls(cloud_account)

# cloud/executors/base.py
from abc import ABC, abstractmethod


class CloudExecutor(ABC):

    def __init__(self, cloud_account):
        self.cloud_account = cloud_account

    @abstractmethod
    def execute(
        self,
        *,
        target_type,
        namespace,
        target_name,
        action,
        parameters,
    ):
        raise NotImplementedError

from abc import ABC, abstractmethod


class CloudAction(ABC):
    """
    Cloud-agnostic action contract.
    """

    @abstractmethod
    def execute(self, session):
        pass

    @abstractmethod
    def rollback(self, session):
        pass

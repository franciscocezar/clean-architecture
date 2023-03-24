from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_user(self, name: str, password: str):
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None):
        """abstractmethod"""

        raise Exception("Method not implemented")

from abc import ABC, abstractmethod


class FindUser(ABC):
    """Interface to FindUser use case"""

    @abstractmethod
    def by_id(cls, user_id):
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def by_name(cls, user_name):
        """Specific Case"""

        raise Exception("Should implement method: by_name")

    @abstractmethod
    def by_id_and_name(cls, user_id, user_name):
        """Specific Case"""

        raise Exception("Should implement method: by_id_and_name")

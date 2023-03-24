from abc import ABC, abstractmethod


class PetRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int):
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def select_pet(self, pet_id: int = None, user_id: int = None):
        """abstractmethod"""

        raise Exception("Method not implemented")

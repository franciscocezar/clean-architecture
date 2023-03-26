from abc import ABC, abstractmethod


class RegisterPet(ABC):
    """Interface to RegisterPet use case"""

    @abstractmethod
    def register(self, name, specie, user_information, age=None):
        """Use case"""
        raise Exception("Should implement method: register")

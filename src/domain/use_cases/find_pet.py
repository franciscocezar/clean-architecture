from abc import ABC, abstractmethod


class FindPet(ABC):
    """Interface to use case find pet"""

    @abstractmethod
    def by_pet_id(self, pet_id):
        """Specific case"""

        raise Exception("Should implement method: by_pet_id")

    @abstractmethod
    def by_user_id(self, user_id):
        """Specific case"""

        raise Exception("Should implement method: by_user_id")

    @abstractmethod
    def by_pet_id_and_user_id(self, pet_id, user_id):
        """Specific case"""

        raise Exception("Should implement method: by_pet_id_and_user_id")

from src.domain.test import mock_pet


class PetRepositorySpy:
    """Spy to Pet Repository"""

    def __init__(self):
        self.insert_pet_params = {}
        self.select_pet_params = {}

    def insert_pet(self, name, specie, age, user_id):
        """Spy to all the attributes"""

        self.insert_pet_params["name"] = name
        self.insert_pet_params["specie"] = specie
        self.insert_pet_params["age"] = age
        self.insert_pet_params["user_id"] = user_id

        return mock_pet()

    def select_pet(self, pet_id, user_id):
        """Spy to all the attributes"""

        self.select_pet_params["pet_id"] = pet_id
        self.select_pet_params["user_id"] = user_id

        return [mock_pet()]

from src.domain.test import mock_pet, mock_users


class RegisterPetSpy:
    """Class to define use case: Register Pet"""

    def __init__(self, pet_repository, find_user):
        self.pet_repository = pet_repository
        self.find_user = find_user
        self.registry_params = {}

    def registry(self, name, specie, user_information, age=None):
        """Regsitry Pet"""

        self.registry_params["name"] = name
        self.registry_params["specie"] = specie
        self.registry_params["user_information"] = user_information
        self.registry_params["age"] = age

        response = None

        # Validating entry and trying to find an user
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = mock_pet()

        return {"Success": checker, "Data": response}

    def __find_user_information(self, user_information):
        """Check user Infos and select user"""

        user_founded = None
        user_params = user_information.keys()

        if "user_id" in user_params and "user_name" in user_params:
            user_founded = {"Success": True, "Data": mock_users()}

        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = {"Success": True, "Data": mock_users()}

        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = {"Success": True, "Data": mock_users()}

        else:
            return {"Success": False, "Data": None}

        return user_founded

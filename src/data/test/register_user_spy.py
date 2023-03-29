from src.domain.test import mock_users


class RegisterUserSpy:
    """Class to define use case: Register User"""

    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.registry_params = {}

    def register(self, name, password):
        """Registry User"""

        self.registry_params["name"] = name
        self.registry_params["password"] = password

        response = None

        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = mock_users()

        return {"Success": validate_entry, "Data": response}

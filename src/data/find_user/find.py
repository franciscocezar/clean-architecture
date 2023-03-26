from typing import Type
from src.domain.use_cases import FindUser as FindUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository


class FindUser(FindUserInterface):
    """Class to define use case Find User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id):
        """Select User by id
        :param - user_id: id of the user
        :return - Dictionary with informations of the process"""

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name):
        """Select User by name
        :param - name: name of the user
        :return - Dictionary with informations of the process"""

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, user_id, name):
        """Select User by id and by name
        :param  - id: id of the user
                - name: name of the user
        :return - Dictionary with informations of the process"""

        response = None
        validate_entry = isinstance(name, str) and isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id, name=name)

        return {"Success": validate_entry, "Data": response}

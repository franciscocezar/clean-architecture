from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterUserController
from src.data.register_user import RegisterUser
from src.infra.repo.user_repository import UserRepository


def register_user_composer() -> RouteInterface:
    """Composing Register User Route
    :param - None
    :reutrn - Object with Register User Route
    """

    repository = UserRepository()
    user_case = RegisterUser(repository)
    register_user_route = RegisterUserController(user_case)

    return register_user_route

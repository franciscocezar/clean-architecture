from faker import Faker
from src.data.test import RegisterUserSpy
from src.infra.test import UserRepositorySpy
from .register_user_controller import RegisterUserController
from src.presenters.helpers import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)

    attributes = {"name": faker.word(), "password": faker.word()}

    response = register_user_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_user_use_case.registry_params["name"] == attributes["name"]
    assert register_user_use_case.registry_params["password"] == attributes["password"]

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_error_no_body():
    """Testing route method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)

    response = register_user_route.route(HttpRequest())

    assert register_user_use_case.registry_params == {}

    assert response.status_code == 400
    assert "error" in response.body


def test_route_error_wrong_body():
    """Testing route method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)

    attributes = {"name": faker.word()}

    response = register_user_route.route(HttpRequest(body=attributes))

    print(response)

    assert register_user_use_case.registry_params == {}

    assert response.status_code == 422
    assert "error" in response.body

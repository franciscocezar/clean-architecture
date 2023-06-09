from faker import Faker
from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy
from .register_pet_controller import RegisterPetController
from src.presenters.helpers import HttpRequest


faker = Faker()


def test_route():
    """Testing route in RegisnterPetController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "dog",
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_route.route(HttpRequest(body=attributes))

    print(response)

    # Testing inputs
    assert register_pet_use_case.registry_params["name"] == attributes["name"]
    assert register_pet_use_case.registry_params["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_params["age"] == attributes["age"]
    assert (
        register_pet_use_case.registry_params["user_information"]
        == attributes["user_information"]
    )

    # Testing outputs
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_error_no_body():
    """Testing route in RegisnterPetController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    response = register_pet_route.route(HttpRequest())

    print(response)

    # Testing inputs
    assert register_pet_use_case.registry_params == {}

    # Testing outputs
    assert response.status_code == 400
    assert "error" in response.body


def test_route_error_wrong_body():
    """Testing route in RegisnterPetController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {"name": faker.word()}

    response = register_pet_route.route(HttpRequest(body=attributes))

    print(response)

    # Testing inputs
    assert register_pet_use_case.registry_params == {}

    # Testing outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_route_error_without_user_information():
    """Testing route in RegisnterPetController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "dog",
        "age": faker.random_number(),
        "user_information": {},
    }

    response = register_pet_route.route(HttpRequest(body=attributes))

    print(response)

    # Testing inputs
    assert register_pet_use_case.registry_params == {}

    # Testing outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_route_error_without_user_id():
    """Testing route in RegisnterPetController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "dog",
        "age": faker.random_number(),
        "user_information": {"user_name": faker.word()},
    }

    response = register_pet_route.route(HttpRequest(body=attributes))

    print(response)

    # Testing inputs
    assert register_pet_use_case.registry_params["name"] == attributes["name"]
    assert register_pet_use_case.registry_params["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_params["age"] == attributes["age"]
    assert (
        register_pet_use_case.registry_params["user_information"]
        == attributes["user_information"]
    )

    # Testing outputs
    assert response.status_code == 200
    assert "error" not in response.body

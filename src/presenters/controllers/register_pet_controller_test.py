from faker import Faker
from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy
from .register_pet_controller import RegisterPetController
from src.presenters.helpers import HttpRequest


faker = Faker()


def test_handle():
    """Testing handle in RegisnterPetController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_handle = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "dog",
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_handle.handle(HttpRequest(body=attributes))

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

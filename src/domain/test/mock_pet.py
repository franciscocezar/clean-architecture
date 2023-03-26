from faker import Faker
from src.domain.models import Pets

faker = Faker()


def mock_pet():
    """Mocking Pets"""

    return Pets(
        id=faker.random_number(5),
        name=faker.word(),
        specie="cat",
        age=faker.random_number(1),
        user_id=faker.random_number(5),
    )

from faker import Faker
from sqlalchemy import text
from src.infra.config.db_config import DBConnectionHandler
from .user_repository import UserRepository
from src.infra.entities import Users as UsersModel

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """Should Insert User"""

    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine().connect()

    new_user = user_repository.insert_user(name, password)

    query_user = engine.execute(
        text(f"SELECT * FROM users WHERE id='{new_user.id}';")
    ).fetchone()

    engine.execute(text("DELETE FROM users WHERE id='{}'".format(new_user.id)))
    engine.commit()
    engine.close()

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password


def test_select_user():
    """Should select a user in Users table and compare it"""

    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()
    data = UsersModel(id=user_id, name=name, password=password)

    engine = db_connection_handler.get_engine().connect()
    engine.execute(
        text(
            f"INSERT INTO users (id, name, password) VALUES ('{user_id}', '{name}', '{password}');"
        )
    )
    engine.commit()

    query_user1 = user_repository.select_user(user_id=user_id)
    query_user2 = user_repository.select_user(name=name)
    query_user3 = user_repository.select_user(user_id=user_id, name=name)

    assert data in query_user1
    assert data in query_user2
    assert data in query_user3

    engine.execute(text(f"DELETE FROM users WHERE id='{user_id}'"))
    engine.commit()
    engine.close()

from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    @classmethod
    def insert_user(cls):
        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Francisco", password="Cezar")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

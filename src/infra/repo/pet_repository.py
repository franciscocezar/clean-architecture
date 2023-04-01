from sqlalchemy.exc import NoResultFound
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets


class PetRepository(PetRepositoryInterface):
    """Class to manage Pet repository"""

    @classmethod
    def insert_pet(cls, name, specie, age, user_id):
        """
        Insert data in PetsEntity entity
        :param - name: pet name
               - specie: Enum with species acepted
               - age: pet age
               - user_id: owner id (FK)
        :return - tuple with new pet inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_pet(cls, pet_id=None, user_id=None):
        """
        Select data in PetEntity entity by id and/or user_id
        :param - pet_id: Id of the pet registry
               - user_id: owner id
        :return - List with Pets selected
        """

        try:
            query_data = None

            if pet_id and not user_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id)
                        .one()
                    )
                    query_data = [data]

            elif not pet_id and user_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    query_data = data

            elif pet_id and user_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id, user_id=user_id)
                        .one()
                    )
                    query_data = [data]

            return query_data
        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None

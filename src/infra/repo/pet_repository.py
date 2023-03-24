from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel
from src.domain.models import Pets


class PetRepository:
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

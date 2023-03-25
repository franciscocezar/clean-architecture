from abc import ABC, abstractmethod


class RegisterUser(ABC):
    """Interface to RegisterUser use case"""

    @abstractmethod
    def register(self, name, password):
        """Case"""

        raise Exception("Should implement method: register")

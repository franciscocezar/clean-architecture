from typing import Type
from src.domain.use_cases import RegisterUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class RegisterUserController:
    """Class to define Route to register user use case"""

    def __init__(self, register_user_use_case: Type[RegisterUser]):
        self.register_user_use_case = register_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        # If body in http_request
        if http_request.body:
            body_params = http_request.body.keys()

            if "name" in body_params and "password" in body_params:
                name = http_request.body["name"]
                password = http_request.body["password"]

                response = self.register_user_use_case.register(
                    name=name, password=password
                )
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.erro_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.erro_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

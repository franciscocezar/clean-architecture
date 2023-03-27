class HttpErrors:
    """Class to define errors in http"""

    @staticmethod
    def erro_422():
        """HTTP 422"""

        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def erro_400():
        """HTTP 400"""

        return {"status_code": 400, "body": {"error": "Bad Request"}}

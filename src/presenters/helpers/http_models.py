class HttpRequest:
    """Class to http_request repesentation"""

    def __init__(self, header=None, body=None, query=None):
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self):
        return (
            f"HttpRequest (header={self.header}, body={self.body}, query={self.query})"
        )


class HttpResponse:
    """Class to http_response representation"""

    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return f"HttpResponse (status_code={self.status_code}, body={self.body})"

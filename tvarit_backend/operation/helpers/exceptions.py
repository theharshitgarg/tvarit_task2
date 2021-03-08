from rest_framework.status import (HTTP_400_BAD_REQUEST,
                                   HTTP_503_SERVICE_UNAVAILABLE,)


class ViewRequestValidator(object):
    def __init__(self, request):
        self._request = request

    @property
    def request(self):
        return self._request

    @property
    def request_headers(self):
        return self.request.headers

    @property
    def validate_headers(self):
        headers = self.request_headers

        try:
            is_version_valid = headers["Api-Version"] in API_VERSIONS
        except KeyError:
            raise InvalidAPIHeaderException()

        return is_version_valid

    def validate(self):
        is_valid = self.validate_headers
        if not is_valid:
            raise InvalidAPIHeaderException()

        return is_valid


class HTTPRequestBaseException(Exception):
    ERROR_CODE = "200001"
    DESCRIPTION = "Invalid Request"
    HTTP_CODE = HTTP_400_BAD_REQUEST
    ERRORS = []

    def __init__(self, error_code=None, desc=None, http_code=None, errors={}, **kwargs):
        self._error_code = error_code or self.ERROR_CODE
        self._description = desc or self.DESCRIPTION
        self._http_code = http_code or HTTP_400_BAD_REQUEST
        self._errors = errors or self.ERRORS

    def __str__(self):
        return self._error_code + " : " + self._description

    def json(self):
        return {
            "code": self._error_code,
            "message": self._description,
            "http_code": self._http_code,
            "errors": self._errors
        }


class InvalidRequestException(HTTPRequestBaseException):
    ERROR_CODE = "200001"
    DESCRIPTION = "Invalid Request"
    HTTP_CODE = HTTP_400_BAD_REQUEST
    ERRORS = []

    def __init__(self, error_code=None, desc=None, http_code=None, errors={}):
        super().__init__(
            error_code or self.ERROR_CODE,
            desc or self.DESCRIPTION,
            http_code or self.HTTP_CODE,
            errors or self.ERRORS
        )


class InvalidHeaderException(InvalidRequestException):

    ERROR_CODE = "200100"
    DESCRIPTION = "Invalid Header"
    HTTP_CODE = HTTP_400_BAD_REQUEST
    ERRORS = []

    def __init__(self):
        super().__init__(self.ERROR_CODE, self.DESCRIPTION, self.HTTP_CODE, self.ERRORS)


class InvalidAPIHeaderException(InvalidHeaderException):
    ERROR_CODE = "200101"
    DESCRIPTION = "Invalid Header"
    HTTP_CODE = HTTP_400_BAD_REQUEST
    ERRORS = []

    def __init__(self):
        super().__init__()


class InvalidNumberException(InvalidRequestException):
    ERROR_CODE = "200310"
    DESCRIPTION = "Invalid Number"
    HTTP_CODE = HTTP_400_BAD_REQUEST
    ERRORS = []

    def __init__(self, error_code=None, desc=None, http_code=None, errors={}):
        super().__init__(
            error_code or self.ERROR_CODE,
            desc or self.DESCRIPTION,
            http_code or self.HTTP_CODE,
            errors or self.ERRORS,
        )

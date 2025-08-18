from .models.client_exception import ClientException



class PaapiError(Exception):
    """Base class for all PAAPI errors."""
    def __init__(self, message=None, code=None, status_code=None):
        super().__init__(message or self.__class__.__name__)
        self.code = code
        self.status_code = status_code
    
    def __str__(self):
        base = super().__str__()
        return f"[{self.code}] {base}" if self.code else base


# client exceptions

class AccessDenied(PaapiError):
    """Raised when access is denied."""
    status_code = 403 # HTTP 403
    code = ClientException.ACCESS_DENIED
    message = ClientException.ACCESS_DENIED


class AccessDeniedAwsUsers(PaapiError):
    """Raised when access is denied."""
    status_code = 403 # HTTP 403
    code = ClientException.ACCESS_DENIED_AWS_USERS
    message = ClientException.ACCESS_DENIED_AWS_USERS


class InvalidAssociate(PaapiError):
    """Raised when associate (partner) validation fails."""
    status_code = 403 # HTTP 403
    code = ClientException.ASSOCIATE_VALIDATION
    message = ClientException.ASSOCIATE_VALIDATION


class IncompleteSignature(PaapiError):
    """Raised when request signature is incomplete."""
    status_code = 400 # HTTP 400
    code = ClientException.INCOMPLETE_SIGNATURE
    message = ClientException.INCOMPLETE_SIGNATURE


class InvalidPartnerTag(PaapiError):
    """Raised when partner tag is invalid."""
    status_code = 400 # HTTP 400
    code = ClientException.INVALID_PARTNER_TAG
    message = ClientException.INVALID_PARTNER_TAG


class InvalidSignature(PaapiError):
    """Raised when request signature is invalid."""
    status_code = 401 # HTTP 401
    code = ClientException.INVALID_SIGNATURE
    message = ClientException.INVALID_SIGNATURE


class TooManyRequests(PaapiError):
    """Raised when request throttling occurs (rate limiting)."""
    status_code = 429 # HTTP 429
    code = ClientException.TOO_MANY_REQUESTS
    message = ClientException.TOO_MANY_REQUESTS


class RequestExpired(PaapiError):
    """Raised when the request timestamp is too old."""
    status_code = 401 # HTTP 401
    code = ClientException.REQUEST_EXPIRED
    message = ClientException.REQUEST_EXPIRED


class InvalidParameterValue(PaapiError):
    """Raised when input validation fails."""
    status_code = 400 # HTTP 400
    code = ClientException.INVALID_PARAMETER_VALUE
    message = ClientException.INVALID_PARAMETER_VALUE


class MissingParameter(PaapiError):
    """Raised when input validation fails."""
    status_code = 400 # HTTP 400
    code = ClientException.MISSING_PARAMETER
    message = ClientException.MISSING_PARAMETER


class UnknownOperation(PaapiError):
    """Raised when an unknown API operation is requested."""
    status_code = 404 # HTTP 404
    code = ClientException.UNKNOWN_OPERATION
    message = ClientException.UNKNOWN_OPERATION


class UnrecognizedClient(PaapiError):
    """Raised when client (e.g., access key) is invalid."""
    status_code = 401 # HTTP 401
    code = ClientException.UNRECOGNIZED_CLIENT
    message = ClientException.UNRECOGNIZED_CLIENT


# package exceptions

class AsinNotFound(PaapiError):
    """Raised if the ASIN for an item is not found."""


class InvalidArgument(PaapiError):
    """Raised when arguments are not correct."""


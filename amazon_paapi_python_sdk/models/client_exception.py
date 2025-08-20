import dataclasses
import typing

from .error_data import ErrorData

@dataclasses.dataclass
class ClientException:
    ACCESS_DENIED = "AccessDenied"                   # AccessDeniedException
    ACCESS_DENIED_AWS_USERS = "AccessDeniedAwsUsers" # AccessDeniedException
    ASSOCIATE_VALIDATION = "InvalidAssociate"
    INCOMPLETE_SIGNATURE = "IncompleteSignature"
    INVALID_PARTNER_TAG = "InvalidPartnerTag"
    INVALID_SIGNATURE = "InvalidSignature"
    TOO_MANY_REQUESTS = "TooManyRequests"
    REQUEST_EXPIRED = "RequestExpired"
    INVALID_PARAMETER_VALUE = "InvalidParameterValue" # ValidationException
    MISSING_PARAMETER = "MissingParameter"            # ValidationException
    UNKNOWN_OPERATION = "UnknownOperation"
    UNRECOGNIZED_CLIENT = "UnrecognizedClient"

    errors: typing.Optional[list[ErrorData]] = dataclasses.field(metadata={'key': 'Errors'})
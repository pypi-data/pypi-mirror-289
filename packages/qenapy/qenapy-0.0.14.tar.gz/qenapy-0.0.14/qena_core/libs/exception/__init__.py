"""
Exception related classes and functions
"""

from ._client_error import *
from ._handler import handle_microservice_exception
from ._microservice_exception import MicroserviceException
from ._rabbitmq_exception import RabbitMQException
from ._redirection_error import *

# disable redefining built-in function
# because of NotImplemented
from ._server_error import *  # pylint: disable=W0622
from ._severity import Severity

__all__ = [
    # client errors
    "BadRequest",
    "Unauthorized",
    "PaymentRequired",
    "Forbidden",
    "NotFound",
    "MethodNotAllowed",
    "NotAcceptable",
    "ProxyAuthenticationRequired",
    "RequestTimeout",
    "Conflict",
    "Gone",
    "LengthRequired",
    "PreconditionFailed",
    "PayloadTooLarge",
    "URITooLong",
    "UnsupportedMediaType",
    "RangeNotSatisfiable",
    "ExpectationFailed",
    "IAmATeapot",
    "MisdirectedRequest",
    "UnprocessableEntity",
    "Locked",
    "FailedDependency",
    "TooEarly",
    "UpgradeRequired",
    "PreconditionRequired",
    "TooManyRequests",
    "RequestHeaderFieldsTooLarge",
    "UnavailableForLegalReasons",
    # redirect errors
    "MultipleChoices",
    "MovedPermanently",
    "Found",
    "SeeOther",
    "NotModified",
    "UseProxy",
    "Unused",
    "TemporaryRedirect",
    "PermanentRedirect",
    # server errors
    "InternalServerError",
    "NotImplemented",
    "BadGateway",
    "ServiceUnavailable",
    "GatewayTimeout",
    "HTTPVersionNotSupported",
    "VariantAlsoNegotiates",
    "InsufficientStorage",
    "LoopDetected",
    "NotExtended",
    "NetworkAuthenticationRequired",
    # microservice exceptions
    "MicroserviceException",
    # rabbitmq exceptions
    "RabbitMQException",
]

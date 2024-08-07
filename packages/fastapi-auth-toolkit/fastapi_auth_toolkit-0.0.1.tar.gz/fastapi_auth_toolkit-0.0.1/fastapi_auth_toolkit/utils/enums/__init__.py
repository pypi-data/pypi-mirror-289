from fastapi_auth_toolkit.utils.enums.auth import AuthExceptionEnum
from fastapi_auth_toolkit.utils.enums.response import ExceptionTypeEnum


class ExceptionsType:
    AUTHENTICATION = AuthExceptionEnum
    RESPONSE = ExceptionTypeEnum


class FastapiAuthEnum:
    EXCEPTIONS = ExceptionsType

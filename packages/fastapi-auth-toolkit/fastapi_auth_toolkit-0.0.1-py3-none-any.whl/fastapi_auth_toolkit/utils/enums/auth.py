from fastapi_auth_toolkit.utils.enums.base import BaseCustomEnum


class AuthExceptionEnum(BaseCustomEnum):
    NOT_AUTHENTICATED = 'Authentication credentials were not provided.'
    PERMISSION_DENIED = 'You do not have permission to perform this action.'
    TOKEN_NOT_VALID = "Token is invalid or expired"

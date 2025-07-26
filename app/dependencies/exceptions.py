"""This module defines custom exceptions."""
from fastapi import HTTPException, status

from app.dependencies import constants


class CannotBeAuthenticatedError(HTTPException):
    """The exception raised when the user cannot be authenticated."""
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=constants.OAUTH2_INVALID_CREDENTIALS,
            headers=constants.JWT_HEADER
        )


class UnauthorizedError(HTTPException):
    """The exception raised when the JWT is invalid."""
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=constants.JWT_INVALID_TOKEN,
            headers=constants.JWT_HEADER,
        )

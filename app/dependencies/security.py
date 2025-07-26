"""This module defines functions related to security of the application."""
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError, InvalidSubjectError

from app.dependencies import constants, exceptions, hashing
from app.models import orm_classes


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")


def authenticate_user(user: orm_classes.Users, plaintext_password: str) -> dict[str, str] | None:
    """Return a dict of user_id and username if the user is authenticated, otherwise return None."""
    if user and hashing.verify(user.password, plaintext_password):
        return {"user_id": user.user_id, "username": user.username}
    return None


def create_access_token(data: dict[str, str | datetime], expiry_in_minutes: int) -> str:
    """Create a JWT access token"""
    expiry = datetime.now(timezone.utc) + timedelta(minutes=expiry_in_minutes)
    to_encode = data.copy()
    to_encode.update({"exp": expiry})
    encoded_jwt = jwt.encode(to_encode, constants.JWT_SECRET_KEY,
                             algorithm=constants.JWT_ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    """Extract the user's identity from the JWT."""
    try:
        payload = jwt.decode(token, constants.JWT_SECRET_KEY,
                             algorithms=[constants.JWT_ALGORITHM])
        identity = payload.get("sub")
        if not identity:
            raise InvalidSubjectError
    except (InvalidTokenError, InvalidSubjectError):
        raise exceptions.UnauthorizedError()
    return identity

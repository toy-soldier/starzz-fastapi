"""This module defines functions related to authentication."""
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.dependencies import constants, exceptions, security
from app.models import crud_and_listing


def handle_login(
        form_data: OAuth2PasswordRequestForm, session: Session) -> dict[str, str]:
    """Handle the login attempt; return a JWT if successful, otherwise raise an error."""
    data = security.authenticate_user(
        crud_and_listing.get_user_by_username(session, form_data.username), form_data.password)
    if not data:
        raise exceptions.CannotBeAuthenticatedError()

    access_token = security.create_access_token(
        data={"sub": f'{data["username"]}, id={data["user_id"]}'},
        expiry_in_minutes=constants.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    return {"access_token": access_token, "token_type": "bearer"}

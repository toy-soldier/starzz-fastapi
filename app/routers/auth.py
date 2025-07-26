"""This module defines the API router to handle requests to /users."""
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.controllers import auth
from app.dependencies import database


router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
)


@router.post("/")
async def login_to_get_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: Session = Depends(database.get_session)) -> dict[str, str]:
    """ Returns a JWT upon successful login. """
    return auth.handle_login(form_data, session)

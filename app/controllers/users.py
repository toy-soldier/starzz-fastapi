"""This module defines the functions called when the *_user* routes are invoked."""
from sqlmodel import Session

from app.dependencies import hashing
from app.models import orm_classes, crud_and_listing
from app.schemas import users as u


def handle_post(session: Session, data: u.UsersForCreate) -> orm_classes.Users:
    """Handle the POST request."""
    encrypt_password(data)
    return crud_and_listing.create(orm_classes.Users, session, data)


def encrypt_password(data: u.UsersForCreate | u.UsersForUpdate) -> None:
    """Encrypt the password before writing it to the database."""
    plaintext_password = getattr(data, "password")
    if plaintext_password:
        setattr(data, "password", hashing.bcrypt(plaintext_password))


def handle_get(session: Session, user_id: int) -> orm_classes.Users:
    """Handle the GET request."""
    return crud_and_listing.retrieve(orm_classes.Users, session, user_id)


def handle_put(session: Session, data: u.UsersForUpdate,
               user_id: int) -> orm_classes.Users:
    """Handle the PUT request."""
    encrypt_password(data)
    return crud_and_listing.update(orm_classes.Users, session, data, user_id)


def handle_delete(session: Session, user_id: int) -> None:
    """Handle the DELETE request."""
    crud_and_listing.delete(orm_classes.Users, session, user_id)


def handle_list(session: Session) -> list[orm_classes.Users]:
    """Handle the GET request."""
    return crud_and_listing.listing(orm_classes.Users, session)

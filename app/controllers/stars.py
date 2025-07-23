"""This module defines the functions called when the *_star* routes are invoked."""
from sqlmodel import Session

from app.models import orm_classes, crud_and_listing
from app.schemas import stars as s


def handle_post(session: Session, data: s.StarsForCreate) -> orm_classes.Stars:
    """Handle the POST request."""
    return crud_and_listing.create(orm_classes.Stars, session, data)


def handle_get(session: Session, star_id: int) -> orm_classes.Stars:
    """Handle the GET request."""
    return crud_and_listing.retrieve(orm_classes.Stars, session, star_id)


def handle_put(session: Session, data: s.StarsForUpdate,
               star_id: int) -> orm_classes.Stars:
    """Handle the PUT request."""
    return crud_and_listing.update(orm_classes.Stars, session, data, star_id)


def handle_delete(session: Session, star_id: int) -> None:
    """Handle the DELETE request."""
    crud_and_listing.delete(orm_classes.Stars, session, star_id)


def handle_list(session: Session) -> list[orm_classes.Stars]:
    """Handle the GET request."""
    return crud_and_listing.listing(orm_classes.Stars, session)

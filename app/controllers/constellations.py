"""This module defines the functions called when the *_constellation* routes are invoked."""
from sqlmodel import Session

from app.models import orm_classes, crud_and_listing
from app.schemas import constellations as c


def handle_post(session: Session, data: c.ConstellationsForCreate) -> orm_classes.Constellations:
    """Handle the POST request."""
    return crud_and_listing.create(orm_classes.Constellations, session, data)


def handle_get(session: Session, constellation_id: int) -> orm_classes.Constellations:
    """Handle the GET request."""
    return crud_and_listing.retrieve(orm_classes.Constellations, session, constellation_id)


def handle_put(session: Session, data: c.ConstellationsForUpdate,
               constellation_id: int) -> orm_classes.Constellations:
    """Handle the PUT request."""
    return crud_and_listing.update(orm_classes.Constellations, session, data, constellation_id)


def handle_delete(session: Session, constellation_id: int) -> None:
    """Handle the DELETE request."""
    crud_and_listing.delete(orm_classes.Constellations, session, constellation_id)


def handle_list(session: Session) -> list[orm_classes.Constellations]:
    """Handle the GET request."""
    return crud_and_listing.listing(orm_classes.Constellations, session)

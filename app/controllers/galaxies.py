"""This module defines the functions called when the *_galaxy* routes are invoked."""
from sqlmodel import Session

from app.models import orm_classes, crud_and_listing
from app.schemas import galaxies as g


def handle_post(session: Session, data: g.GalaxiesForCreate) -> orm_classes.Galaxies:
    """Handle the POST request."""
    return crud_and_listing.create(orm_classes.Galaxies, session, data)


def handle_get(session: Session, galaxy_id: int) -> orm_classes.Galaxies:
    """Handle the GET request."""
    return crud_and_listing.retrieve(orm_classes.Galaxies, session, galaxy_id)


def handle_put(session: Session, data: g.GalaxiesForUpdate,
               galaxy_id: int) -> orm_classes.Galaxies:
    """Handle the PUT request."""
    return crud_and_listing.update(orm_classes.Galaxies, session, data, galaxy_id)


def handle_delete(session: Session, galaxy_id: int) -> None:
    """Handle the DELETE request."""
    crud_and_listing.delete(orm_classes.Galaxies, session, galaxy_id)


def handle_list(session: Session) -> list[orm_classes.Galaxies]:
    """Handle the GET request."""
    return crud_and_listing.listing(orm_classes.Galaxies, session)

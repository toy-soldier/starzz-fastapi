"""This module contains functions to perform CRUD and listing operations."""
from fastapi import HTTPException
from sqlmodel import Session, select

from app.dependencies import constants
from app.models.orm_classes import Constellations, Galaxies, Stars, Users
from app.schemas import constellations as c
from app.schemas import galaxies as g
from app.schemas import stars as s
from app.schemas import users as u


MODELS = Constellations | Galaxies | Stars | Users
MODEL_CLASSES = (Constellations.__class__ | Galaxies.__class__ |
                 Stars.__class__ | Users.__class__)
SCHEMAS_FOR_CREATE = (c.ConstellationsForCreate | g.GalaxiesForCreate |
                      s.StarsForCreate | u.UsersForCreate)
SCHEMAS_FOR_UPDATE = (c.ConstellationsForUpdate | g.GalaxiesForUpdate |
                      s.StarsForUpdate | u.UsersForUpdate)


def create(class_: MODEL_CLASSES,
           session: Session, data: SCHEMAS_FOR_CREATE) -> MODELS:
    """The Create operation."""
    new_obj = class_.model_validate(data)
    session.add(new_obj)
    session.commit()
    session.refresh(new_obj)
    return new_obj


def retrieve(class_: MODEL_CLASSES, session: Session, obj_id: int) -> MODELS:
    """The Retrieve operation."""
    existing_obj = session.get(class_, obj_id)
    if not existing_obj:
        raise HTTPException(status_code=404,
                            detail=constants.ERROR_NOT_FOUND.format(class_.__name__))
    return existing_obj


def update(class_: MODEL_CLASSES, session: Session, data: SCHEMAS_FOR_UPDATE,
               obj_id: int) -> MODELS:
    """The Update operation."""
    existing_obj = retrieve(class_, session, obj_id)
    new_data = data.model_dump(exclude_unset=True)
    existing_obj.sqlmodel_update(new_data)
    session.add(existing_obj)
    session.commit()
    session.refresh(existing_obj)
    return existing_obj


def delete(class_: MODEL_CLASSES, session: Session, obj_id: int) -> None:
    """The Delete operation."""
    existing_obj = retrieve(class_, session, obj_id)
    session.delete(existing_obj)
    session.commit()


def listing(class_: MODEL_CLASSES, session: Session) -> list[MODELS]:
    """The Listing operation."""
    return session.exec(select(class_)).all()

"""This module defines the API router to handle requests to /constellations."""
from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.dependencies import database
from app.controllers import constellations
from app.models import orm_classes
from app.schemas import constellations as c


router = APIRouter(
    prefix="/constellations",
    tags=["constellations"],
)

@router.get("/", status_code=status.HTTP_200_OK,
            response_model=list[c.ConstellationsShortInfo])
async def list_constellations(
        session: Session = Depends(database.get_session)) -> list[orm_classes.Constellations]:
    """The return is actually a list of the models but is converted to the desired schema."""
    return constellations.handle_list(session)


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=c.ConstellationsLongInfo)
async def register_constellation(data: c.ConstellationsForCreate,
                                 session: Session = Depends(database.get_session)
                                 ) -> orm_classes.Constellations:
    """The return is actually the model but is converted to the desired schema."""
    return constellations.handle_post(session, data)


@router.get("/{constellation_id}", status_code=status.HTTP_200_OK,
            response_model=c.ConstellationsLongInfo)
async def get_constellation(constellation_id: int,
                            session: Session = Depends(database.get_session)
                            ) -> orm_classes.Constellations:
    """The return is actually the model but is converted to the desired schema."""
    return constellations.handle_get(session, constellation_id)


@router.put("/{constellation_id}", status_code=status.HTTP_202_ACCEPTED,
            response_model=c.ConstellationsLongInfo)
async def update_constellation(constellation_id: int, data: c.ConstellationsForUpdate,
                               session: Session = Depends(database.get_session)
                               ) -> orm_classes.Constellations:
    """The return is actually the model but is converted to the desired schema."""
    return constellations.handle_put(session, data, constellation_id)


@router.delete("/{constellation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_constellation(constellation_id: int,
                               session: Session = Depends(database.get_session)) -> None:
    """Handle DELETE method."""
    return constellations.handle_delete(session, constellation_id)

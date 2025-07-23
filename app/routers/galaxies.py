"""This module defines the API router to handle requests to /galaxies."""
from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.dependencies import database
from app.controllers import galaxies
from app.models import orm_classes
from app.schemas import galaxies as g

router = APIRouter(
    prefix="/galaxies",
    tags=["galaxies"],
)


@router.get("/", status_code=status.HTTP_200_OK,
            response_model=list[g.GalaxiesShortInfo])
async def list_galaxies(
        session: Session = Depends(database.get_session)) -> list[orm_classes.Galaxies]:
    """The return is actually a list of the models but is converted to the desired schema."""
    return galaxies.handle_list(session)


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=g.GalaxiesLongInfo)
async def register_galaxy(data: g.GalaxiesForCreate,
                          session: Session = Depends(database.get_session)
                          ) -> orm_classes.Galaxies:
    """The return is actually the model but is converted to the desired schema."""
    return galaxies.handle_post(session, data)


@router.get("/{galaxy_id}", status_code=status.HTTP_200_OK,
            response_model=g.GalaxiesLongInfo)
async def get_galaxy(galaxy_id: int,
                     session: Session = Depends(database.get_session)
                     ) -> orm_classes.Galaxies:
    """The return is actually the model but is converted to the desired schema."""
    return galaxies.handle_get(session, galaxy_id)


@router.put("/{galaxy_id}", status_code=status.HTTP_202_ACCEPTED,
            response_model=g.GalaxiesLongInfo)
async def update_galaxy(galaxy_id: int, data: g.GalaxiesForUpdate,
                        session: Session = Depends(database.get_session)
                        ) -> orm_classes.Galaxies:
    """The return is actually the model but is converted to the desired schema."""
    return galaxies.handle_put(session, data, galaxy_id)


@router.delete("/{galaxy_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_galaxy(galaxy_id: int,
                        session: Session = Depends(database.get_session)) -> None:
    """Handle DELETE method."""
    return galaxies.handle_delete(session, galaxy_id)

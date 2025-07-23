"""This module defines the API router to handle requests to /stars."""
from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.dependencies import database
from app.controllers import stars
from app.models import orm_classes
from app.schemas import stars as s

router = APIRouter(
    prefix="/stars",
    tags=["stars"],
)


@router.get("/", status_code=status.HTTP_200_OK,
            response_model=list[s.StarsShortInfo])
async def list_stars(
        session: Session = Depends(database.get_session)) -> list[orm_classes.Stars]:
    """The return is actually a list of the models but is converted to the desired schema."""
    return stars.handle_list(session)


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=s.StarsLongInfo)
async def register_star(data: s.StarsForCreate,
                        session: Session = Depends(database.get_session)
                        ) -> orm_classes.Stars:
    """The return is actually the model but is converted to the desired schema."""
    return stars.handle_post(session, data)


@router.get("/{star_id}", status_code=status.HTTP_200_OK,
            response_model=s.StarsLongInfo)
async def get_star(star_id: int,
                   session: Session = Depends(database.get_session)
                   ) -> orm_classes.Stars:
    """The return is actually the model but is converted to the desired schema."""
    return stars.handle_get(session, star_id)


@router.put("/{star_id}", status_code=status.HTTP_202_ACCEPTED,
            response_model=s.StarsLongInfo)
async def update_star(star_id: int, data: s.StarsForUpdate,
                      session: Session = Depends(database.get_session)
                      ) -> orm_classes.Stars:
    """The return is actually the model but is converted to the desired schema."""
    return stars.handle_put(session, data, star_id)


@router.delete("/{star_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_star(star_id: int,
                      session: Session = Depends(database.get_session)) -> None:
    """Handle DELETE method."""
    return stars.handle_delete(session, star_id)

"""This module defines the API router to handle requests to /users."""
from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.dependencies import database, security
from app.controllers import users
from app.models import orm_classes
from app.schemas import users as u

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/", status_code=status.HTTP_200_OK,
            response_model=list[u.UsersShortInfo])
async def list_users(
        session: Session = Depends(database.get_session)) -> list[orm_classes.Users]:
    """The return is actually a list of the models but is converted to the desired schema."""
    return users.handle_list(session)


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=u.UsersLongInfo)
async def register_user(data: u.UsersForCreate,
                        session: Session = Depends(database.get_session),
                        _: str = Depends(security.get_current_user)
                        ) -> orm_classes.Users:
    """The return is actually the model but is converted to the desired schema."""
    return users.handle_post(session, data)


@router.get("/{user_id}", status_code=status.HTTP_200_OK,
            response_model=u.UsersLongInfo)
async def get_user(user_id: int,
                   session: Session = Depends(database.get_session)
                   ) -> orm_classes.Users:
    """The return is actually the model but is converted to the desired schema."""
    return users.handle_get(session, user_id)


@router.put("/{user_id}", status_code=status.HTTP_202_ACCEPTED,
            response_model=u.UsersLongInfo)
async def update_user(user_id: int, data: u.UsersForUpdate,
                      session: Session = Depends(database.get_session),
                      _: str = Depends(security.get_current_user)
                      ) -> orm_classes.Users:
    """The return is actually the model but is converted to the desired schema."""
    return users.handle_put(session, data, user_id)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int,
                      session: Session = Depends(database.get_session),
                      _: str = Depends(security.get_current_user)
                      ) -> None:
    """Handle DELETE method."""
    return users.handle_delete(session, user_id)

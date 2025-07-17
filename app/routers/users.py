"""This module defines the API router to handle requests to /users."""
from fastapi import APIRouter, status

from app.controllers import users


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register_user() -> dict[str, str]:
    """Handle POST method."""
    return users.handle_post()


@router.get("/", status_code=status.HTTP_200_OK)
async def list_users() -> dict[str, str]:
    """Handle GET method."""
    return users.handle_list()


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: int) -> dict[str, str | int]:
    """Handle GET method."""
    return users.handle_get(user_id)


@router.put("/{user_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(user_id: int) -> dict[str, str | int]:
    """Handle PUT method."""
    return users.handle_put(user_id)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str) -> None:
    """Handle DELETE method."""
    return users.handle_delete(user_id)

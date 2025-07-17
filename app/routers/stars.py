"""This module defines the API router to handle requests to /stars."""
from fastapi import APIRouter, status

from app.controllers import stars


router = APIRouter(
    prefix="/stars",
    tags=["stars"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register_star() -> dict[str, str]:
    """Handle POST method."""
    return stars.handle_post()


@router.get("/", status_code=status.HTTP_200_OK)
async def list_stars() -> dict[str, str]:
    """Handle GET method."""
    return stars.handle_list()


@router.get("/{star_id}", status_code=status.HTTP_200_OK)
async def get_star(star_id: int) -> dict[str, str | int]:
    """Handle GET method."""
    return stars.handle_get(star_id)


@router.put("/{star_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_star(star_id: int) -> dict[str, str | int]:
    """Handle PUT method."""
    return stars.handle_put(star_id)


@router.delete("/{star_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_star(star_id: str) -> None:
    """Handle DELETE method."""
    return stars.handle_delete(star_id)

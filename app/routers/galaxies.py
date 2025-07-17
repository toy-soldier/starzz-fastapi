"""This module defines the API router to handle requests to /galaxies."""
from fastapi import APIRouter, status

from app.controllers import galaxies


router = APIRouter(
    prefix="/galaxies",
    tags=["galaxies"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register_galaxy() -> dict[str, str]:
    """Handle POST method."""
    return galaxies.handle_post()


@router.get("/", status_code=status.HTTP_200_OK)
async def list_galaxies() -> dict[str, str]:
    """Handle GET method."""
    return galaxies.handle_list()


@router.get("/{galaxy_id}", status_code=status.HTTP_200_OK)
async def get_galaxy(galaxy_id: int) -> dict[str, str | int]:
    """Handle GET method."""
    return galaxies.handle_get(galaxy_id)


@router.put("/{galaxy_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_galaxy(galaxy_id: int) -> dict[str, str | int]:
    """Handle PUT method."""
    return galaxies.handle_put(galaxy_id)


@router.delete("/{galaxy_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_galaxy(galaxy_id: str) -> None:
    """Handle DELETE method."""
    return galaxies.handle_delete(galaxy_id)

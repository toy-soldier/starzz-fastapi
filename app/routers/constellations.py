"""This module defines the API router to handle requests to /constellations."""
from fastapi import APIRouter, status

from app.controllers import constellations


router = APIRouter(
    prefix="/constellations",
    tags=["constellations"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register_constellation() -> dict[str, str]:
    """Handle POST method."""
    return constellations.handle_post()


@router.get("/", status_code=status.HTTP_200_OK)
async def list_constellations() -> dict[str, str]:
    """Handle GET method."""
    return constellations.handle_list()


@router.get("/{constellation_id}", status_code=status.HTTP_200_OK)
async def get_constellation(constellation_id: int) -> dict[str, str | int]:
    """Handle GET method."""
    return constellations.handle_get(constellation_id)


@router.put("/{constellation_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_constellation(constellation_id: int) -> dict[str, str | int]:
    """Handle PUT method."""
    return constellations.handle_put(constellation_id)


@router.delete("/{constellation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_constellation(constellation_id: str) -> None:
    """Handle DELETE method."""
    return constellations.handle_delete(constellation_id)

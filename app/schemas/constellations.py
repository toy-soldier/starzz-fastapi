"""This module defines the classes to be used in the /constellations routes."""
from sqlmodel import Field, SQLModel

from app.schemas import users as u, galaxies as g


class ConstellationsBase(SQLModel):
    """Base class for Constellations* schemas."""
    constellation_name: str = Field(index=True)


class ConstellationsForCreate(ConstellationsBase):
    """Class to be used for adding a new Constellations object."""
    galaxy_id: int
    added_by: int
    verified_by: int | None = None


class ConstellationsForUpdate(ConstellationsBase):
    """Class to be used for updating an existing Constellations object."""
    constellation_name: str | None = None
    galaxy_id: int | None = None
    added_by: int | None = None
    verified_by: int | None = None


class ConstellationsShortInfo(ConstellationsBase):
    """Class to be used for displaying a Constellation's short info."""
    constellation_id: int


class ConstellationsLongInfo(ConstellationsBase):
    """Class to be used for displaying a Constellation's complete info."""
    constellation_id: int
    galaxy_info: g.GalaxiesShortInfo
    added_by_info: u.UsersShortInfo
    verified_by_info: u.UsersShortInfo | None

"""This module defines the classes to be used in the /stars routes."""
from sqlmodel import Field, SQLModel

from app.schemas import users as u, constellations as c

class StarsBase(SQLModel):
    """Base class for Stars* schemas."""
    star_name: str = Field(index=True)


class StarsForCreate(StarsBase):
    """Class to be used for adding a new Stars object."""
    star_type: str
    constellation_id: int
    right_ascension: int
    declination: int
    apparent_magnitude: int
    spectral_type: str
    added_by: int
    verified_by: int | None = None


class StarsForUpdate(StarsBase):
    """Class to be used for updating an existing Stars object."""
    star_name: str | None = None
    star_type: str | None = None
    constellation_id: int | None = None
    right_ascension: int | None = None
    declination: int | None = None
    apparent_magnitude: int | None = None
    spectral_type: str | None = None
    added_by: int | None = None
    verified_by: int | None = None


class StarsShortInfo(StarsBase):
    """Class to be used for displaying a Star's short info."""
    star_id: int


class StarsLongInfo(StarsBase):
    """Class to be used for displaying a Star's complete info."""
    star_id: int
    star_type: str
    right_ascension: int
    declination: int
    apparent_magnitude: int
    spectral_type: str
    constellation_info: c.ConstellationsShortInfo
    added_by_info: u.UsersShortInfo
    verified_by_info: u.UsersShortInfo | None

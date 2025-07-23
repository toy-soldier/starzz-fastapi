"""This module defines the classes to be used in the /galaxies routes."""
from sqlmodel import Field, SQLModel

from app.schemas import users as u


class GalaxiesBase(SQLModel):
    """Base class for Galaxies* schemas."""
    galaxy_name: str = Field(index=True)


class GalaxiesCommons(GalaxiesBase):
    """Class having some common fields of Galaxies objects and `galaxies` table rows."""
    galaxy_type: str
    distance_mly: int
    redshift: int
    mass_solar: int
    diameter_ly: int


class GalaxiesForCreate(GalaxiesCommons):
    """Class to be used for adding a new Galaxies object."""
    added_by: int
    verified_by: int | None = None


class GalaxiesForUpdate(GalaxiesBase):
    """Class to be used for updating an existing Galaxies object."""
    galaxy_name: str | None = None
    galaxy_type: str | None = None
    distance_mly: int | None = None
    redshift: int | None = None
    mass_solar: int | None = None
    diameter_ly: int | None = None
    added_by: int | None = None
    verified_by: int | None = None


class GalaxiesShortInfo(GalaxiesBase):
    """Class to be used for displaying a Galaxy's short info."""
    galaxy_id: int


class GalaxiesLongInfo(GalaxiesBase):
    """Class to be used for displaying a Galaxy's complete info."""
    galaxy_id: int
    galaxy_type: str
    distance_mly: int
    redshift: int
    mass_solar: int
    diameter_ly: int
    added_by_info: u.UsersShortInfo
    verified_by_info: u.UsersShortInfo | None

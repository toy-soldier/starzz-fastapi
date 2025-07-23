"""This module defines all the models for the CRUD operations."""
from sqlmodel import Field, Relationship

from app.dependencies import constants
from app.schemas.constellations import ConstellationsBase
from app.schemas.galaxies import GalaxiesCommons
from app.schemas.stars import StarsBase
from app.schemas.users import UsersForCreate


class Users(UsersForCreate, table=True):
    """ORM class for users table."""
    user_id: int | None = Field(default=None, primary_key=True)

    galaxies_added: list["Galaxies"] = Relationship(
        back_populates="added_by_info",
        sa_relationship_kwargs={"foreign_keys": "Galaxies.added_by"})
    galaxies_verified: list["Galaxies"] = Relationship(
        back_populates="verified_by_info",
        sa_relationship_kwargs={"foreign_keys": "Galaxies.verified_by"})
    constellations_added: list["Constellations"] = Relationship(
        back_populates="added_by_info",
        sa_relationship_kwargs={"foreign_keys": "Constellations.added_by"})
    constellations_verified: list["Constellations"] = Relationship(
        back_populates="verified_by_info",
        sa_relationship_kwargs={"foreign_keys": "Constellations.verified_by"})
    stars_added: list["Stars"] = Relationship(
        back_populates="added_by_info",
        sa_relationship_kwargs={"foreign_keys": "Stars.added_by"})
    stars_verified: list["Stars"] = Relationship(
        back_populates="verified_by_info",
        sa_relationship_kwargs={"foreign_keys": "Stars.verified_by"})


class Galaxies(GalaxiesCommons, table=True):
    """ORM class for galaxies table."""
    galaxy_id: int | None = Field(default=None, primary_key=True)
    added_by: int = Field(foreign_key=constants.USER_ID)
    verified_by: int | None = Field(default=None, foreign_key=constants.USER_ID)

    added_by_info: Users = Relationship(
        back_populates="galaxies_added",
        sa_relationship_kwargs = {"foreign_keys": "Galaxies.added_by"})
    verified_by_info: Users | None = Relationship(
        back_populates="galaxies_verified",
        sa_relationship_kwargs={"foreign_keys": "Galaxies.verified_by"})

    members: list["Constellations"] = Relationship(back_populates="galaxy_info")


class Constellations(ConstellationsBase, table=True):
    """ORM class for constellations table."""
    constellation_id: int | None = Field(default=None, primary_key=True)
    galaxy_id: int = Field(foreign_key="galaxies.galaxy_id")
    added_by: int = Field(foreign_key=constants.USER_ID)
    verified_by: int | None = Field(default=None, foreign_key=constants.USER_ID)

    galaxy_info: Galaxies = Relationship(back_populates="members")
    added_by_info: Users = Relationship(
        back_populates="constellations_added",
        sa_relationship_kwargs = {"foreign_keys": "Constellations.added_by"})
    verified_by_info: Users | None = Relationship(
        back_populates="constellations_verified",
        sa_relationship_kwargs={"foreign_keys": "Constellations.verified_by"})

    members: list["Stars"] = Relationship(back_populates="constellation_info")


class Stars(StarsBase, table=True):
    """ORM class for stars table."""
    star_id: int | None = Field(default=None, primary_key=True)
    star_type: str
    constellation_id: int = Field(foreign_key="constellations.constellation_id")
    right_ascension: int
    declination: int
    apparent_magnitude: int
    spectral_type: str
    added_by: int = Field(foreign_key=constants.USER_ID)
    verified_by: int | None = Field(default=None, foreign_key=constants.USER_ID)

    constellation_info: Constellations = Relationship(back_populates="members")
    added_by_info: Users = Relationship(
        back_populates="stars_added",
        sa_relationship_kwargs = {"foreign_keys": "Stars.added_by"})
    verified_by_info: Users | None = Relationship(
        back_populates="stars_verified",
        sa_relationship_kwargs={"foreign_keys": "Stars.verified_by"})

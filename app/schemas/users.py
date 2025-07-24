"""This module defines the classes to be used in the /users routes."""
from sqlmodel import Field, SQLModel


class UsersBase(SQLModel):
    """Base class for Users* schemas."""
    username: str = Field(index=True)


class UsersForCreate(UsersBase):
    """Class to be used for adding a new Users object."""
    email: str
    password: str
    first_name: str
    last_name: str
    date_of_birth: str


class UsersForUpdate(UsersBase):
    """Class to be used for updating an existing Users object."""
    username: str | None = None
    email: str | None = None
    password: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: str | None = None


class UsersShortInfo(UsersBase):
    """Class to be used for displaying a User's short info."""
    user_id: int


class UsersLongInfo(UsersShortInfo):
    """Class to be used for displaying a User's complete info."""
    email: str
    first_name: str
    last_name: str
    date_of_birth: str

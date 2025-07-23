"""Ths module is responsible for the application's integration with the database."""
import pathlib
from typing import Any, Generator

from sqlmodel import Session, create_engine

from app.dependencies import constants

# allow FastAPI to use the same SQLite database in different threads
connect_args = {'check_same_thread': False}

basedir = pathlib.Path(__file__).parent.resolve()

# specify the location of the database file
DATABASE_URI = constants.SQLITE_URI.format(basedir)

engine = create_engine(DATABASE_URI, connect_args=connect_args, echo=True)

def get_session() -> Generator[Session, Any, None]:
    """Yield a database session."""
    with Session(engine) as session:
        yield session

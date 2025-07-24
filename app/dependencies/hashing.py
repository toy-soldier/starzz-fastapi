"""Module for hashing and verifying passwords."""
from passlib.context import CryptContext


pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def bcrypt(password: str) -> str:
    """Return a hash of the password."""
    return pwd_ctx.hash(password)


def verify(hashed_password: str, plaintext_string: str) -> bool:
    """Check whether the given plaintext string equals the hashed password."""
    return pwd_ctx.verify(plaintext_string, hashed_password)

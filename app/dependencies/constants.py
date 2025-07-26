"""This module contains application constants."""
SQLITE_URI = "sqlite:///{}/db.sqlite3"

ERROR_NOT_FOUND = "{} object not found."
USER_ID = "users.user_id"

OAUTH2_INVALID_CREDENTIALS = "Invalid credentials."
JWT_INVALID_TOKEN = "The JWT is invalid."

JWT_SECRET_KEY = "this_is_a_very_secret_key"
JWT_ALGORITHM = "HS256"
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 30
JWT_HEADER = {"WWW-Authenticate": "Bearer"}

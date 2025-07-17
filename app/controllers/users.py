"""This module defines the functions called when the *_user* routes are invoked."""


def handle_post() -> dict[str, str]:
    """Handle the POST request."""
    return {
        "message": "User successfully registered."
    }


def handle_get(user_id: int) -> dict[str, str | int]:
    """Handle the GET request."""
    return {
        "input": user_id,
        "message": "User successfully retrieved."
    }


def handle_put(user_id: int) -> dict[str, str | int]:
    """Handle the PUT request."""
    return {
        "input": user_id,
        "message": "User successfully updated."
    }


def handle_delete(user_id: int) -> None:
    """Handle the DELETE request."""
    return None


def handle_list() -> dict[str, str]:
    """Handle the GET request."""
    return {
        "input": "ALL",
        "message": "Users successfully retrieved."
    }

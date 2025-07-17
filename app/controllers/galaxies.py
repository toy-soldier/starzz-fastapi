"""This module defines the functions called when the *_galaxy* routes are invoked."""


def handle_post() -> dict[str, str]:
    """Handle the POST request."""
    return {
        "message": "Galaxy successfully registered."
    }


def handle_get(galaxy_id: int) -> dict[str, str | int]:
    """Handle the GET request."""
    return {
        "input": galaxy_id,
        "message": "Galaxy successfully retrieved."
    }


def handle_put(galaxy_id: int) -> dict[str, str | int]:
    """Handle the PUT request."""
    return {
        "input": galaxy_id,
        "message": "Galaxy successfully updated."
    }


def handle_delete(galaxy_id: int) -> None:
    """Handle the DELETE request."""
    return None


def handle_list() -> dict[str, str]:
    """Handle the GET request."""
    return {
        "input": "ALL",
        "message": "Galaxies successfully retrieved."
    }

"""This module defines the functions called when the *_constellation* routes are invoked."""


def handle_post() -> dict[str, str]:
    """Handle the POST request."""
    return {
        "message": "Constellation successfully registered."
    }


def handle_get(constellation_id: int) -> dict[str, str | int]:
    """Handle the GET request."""
    return {
        "input": constellation_id,
        "message": "Constellation successfully retrieved."
    }


def handle_put(constellation_id: int) -> dict[str, str | int]:
    """Handle the PUT request."""
    return {
        "input": constellation_id,
        "message": "Constellation successfully updated."
    }


def handle_delete(constellation_id: int) -> None:
    """Handle the DELETE request."""
    return None


def handle_list() -> dict[str, str]:
    """Handle the GET request."""
    return {
        "input": "ALL",
        "message": "Constellations successfully retrieved."
    }

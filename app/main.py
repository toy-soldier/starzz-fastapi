"""This is the main module of our application."""
from fastapi import FastAPI
import uvicorn

from app.routers import auth, constellations, galaxies, stars, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(constellations.router)
app.include_router(galaxies.router)
app.include_router(stars.router)
app.include_router(users.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

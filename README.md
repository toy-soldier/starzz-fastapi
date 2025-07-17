# starzz-fastapi

This is a REST API backend created using Python's FastAPI framework.

### The Dataset

This project uses a database of fictional galaxies, constellations and stars.  

Here is a diagram to describe the tables and their relationships:

<img src="assets/schema.png" width="500" height="200"/>

Stars are located in constellations, which are in turn located in galaxies.

The `galaxies`, `constellations` and `stars` tables contain the additional
fields `added_by` and `verified_by` to indicate the id of the users who made
the finding and verified it, respectively.

The database was created using SQLite.  The scripts to create the tables and
load the dummy data are included in `assets` for reference.  Note that the primary
keys of each table should actually increment automatically but are simply defined
as `INTEGER` and `PRIMARY KEY`, like so:

    CREATE TABLE users (
        user_id INTEGER,
        ...
        PRIMARY KEY (user_id)
    );
    
    CREATE TABLE galaxies (
        galaxy_id INTEGER,
        ...
        PRIMARY KEY (galaxy_id),
        ...
    );
    
    CREATE TABLE constellations (
        constellation_id INTEGER,
    ...
    PRIMARY KEY (constellation_id),
    );
    
    CREATE TABLE stars (
        star_id INTEGER,
        ...
        PRIMARY KEY (star_id),
        ...
    );

because in SQLite, if a column is defined as `INTEGER` 
and `PRIMARY KEY`, there is no need to 
define it as `AUTO_INCREMENT`.


### The Application

All code committed at each chapter is available with the commit message of the chapter name.

#### Chapter 1: Setting up the routes

Python libraries added:

    fastapi
    uvicorn

We set up the project structure as follows:

    assets           -> contains the application's assets
    app              
    |_ main.py       -> the main module for the application
    |_ controllers   -> modules to handle application logic
    |_ routers       -> modules to handle application requests

The module `main.py` contains code to dispatch the requests to the application, to the classes 
in `routers`:

    ...
    from routers import constellations, galaxies, stars, users
    
    app = FastAPI()
    
    app.include_router(constellations.router)
    app.include_router(galaxies.router)
    app.include_router(stars.router)
    app.include_router(users.router)
    ...

A sample module in the `routers` package is `users.py`.  It contains the functions to 
handle the requests to the `/users` endpoints:

    ...
    from app.controllers import users
    
    
    router = APIRouter(
        prefix="/users",
        tags=["users"],
    )
    
    
    @router.post("/", status_code=status.HTTP_201_CREATED)
    async def register_user() -> dict[str, str]:
        """Handle POST method."""
        return users.handle_post()
    
    
    @router.get("/", status_code=status.HTTP_200_OK)
    async def list_users() -> dict[str, str]:
        """Handle GET method."""
        return users.handle_list()
    ...

The different requests are then forwarded to different functions in `users.py` in the `controllers` package.

    ...
    def handle_post() -> dict[str, str]:
        """Handle the POST request."""
        return {
            "message": "User successfully registered."
        }


    def handle_list() -> dict[str, str]:
        """Handle the GET request."""
        return {
            "input": "ALL",
            "message": "Users successfully retrieved."
        } 
    ...

The other modules in the `routers` package follow a similar logic.

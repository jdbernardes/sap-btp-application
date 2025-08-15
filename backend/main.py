import os

from fastapi import FastAPI

# This block is necessary to handle the differences on how we run the project locally and how we run the project on CF
try:
    from routes import root as root_mod
    from routes import users as users_mod
except ModuleNotFoundError:
    from backend.routes import root as root_mod
    from backend.routes import users as users_mod



app = FastAPI()
app.include_router(root_mod.router)
app.include_router(users_mod.router)
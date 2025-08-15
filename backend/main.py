import os

from fastapi import FastAPI
from routes import root as root_mod
from routes import users as users_mod

## Normaly this will not be needed but was a solution for this project so I won't need to change all folder structure
#try:
#    from routes import root as root_mod
#    from routes import users as users_mod
#except ModuleNotFoundError:
#    from routes import root as root_mod
#    from routes import users as users_mod



app = FastAPI()
app.include_router(root_mod.router)
app.include_router(users_mod.router)
import os

from fastapi import FastAPI
from dotenv import load_dotenv
from backend.routes import root as root_mod
from backend.routes import users as users_mod

# Load .env from backend/.env
load_dotenv()
print("VCAP_SERVICES loaded:", os.getenv("TEST2"))

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
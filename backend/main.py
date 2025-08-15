import os
import json

from fastapi import FastAPI
from pathlib import Path

# This block is necessary to handle the differences on how we run the project locally and how we run the project on CF
try:
    from routes import root as root_mod
    from routes import users as users_mod
except ModuleNotFoundError:
    from backend.routes import root as root_mod
    from backend.routes import users as users_mod
    vcap_path = Path(__file__).parent.parent / "destinations" / "vcap_service.json"
    with open(vcap_path, encoding="utf-8-sig") as f:
        vcap_data = json.load(f)
        os.environ["VCAP_SERVICES"] = json.dumps(vcap_data)




app = FastAPI()
app.include_router(root_mod.router)
app.include_router(users_mod.router)
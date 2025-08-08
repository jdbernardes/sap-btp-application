from fastapi import FastAPI
from backend.app import root

app = FastAPI()
app.include_router(root.router)
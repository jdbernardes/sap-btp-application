from fastapi import FastAPI
from app import root

app = FastAPI()
app.include_router(root.router)
from fastapi import FastAPI
from routes import router
from config import settings

app = FastAPI(title="SAP BTP Backend", docs_url="/docs")

app.include_router(router)

# Add custom startup/shutdown tasks here if needed

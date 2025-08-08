from dotenv import load_dotenv, find_dotenv
import os

# Load .env locally (skipped on Cloud Foundry)
load_dotenv(find_dotenv())

class Settings:
    ENV = os.getenv("ENV", "dev")
    SFSF_BASE_URL = os.getenv("SFSF_BASE_URL", "")
    SFSF_CLIENT_ID = os.getenv("SFSF_CLIENT_ID", "")
    SFSF_CLIENT_SECRET = os.getenv("SFSF_CLIENT_SECRET", "")

settings = Settings()
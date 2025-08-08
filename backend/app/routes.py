from fastapi import APIRouter
from services import get_greeting, get_status

router = APIRouter()

@router.get("/health")
def health():
    return get_status()

@router.get("/hello")
def hello():
    return get_greeting()

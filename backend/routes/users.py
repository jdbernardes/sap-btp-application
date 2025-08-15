from fastapi import APIRouter
try:
    from .services.sfsf_api import get_random_user
except ModuleNotFoundError:
    from services.sfsf_api import get_random_user
router = APIRouter(prefix = '/users', tags = ['Users'])


@router.get("/random-user")
def get_user():
    return get_random_user()
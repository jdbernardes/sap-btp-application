from fastapi import APIRouter

# this try catch block is needed to treat the different file structures in CloudFoundry
try:
    from backend.services.sfsf_api import get_random_user 
except ModuleNotFoundError:
    from services.sfsf_api import get_random_user


router = APIRouter(prefix = '/users', tags = ['Users'])


@router.get("/random-user")
def get_user():
    return get_random_user()
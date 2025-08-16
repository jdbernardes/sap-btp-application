import json
from http import HTTPStatus
from fastapi import APIRouter

# this try catch block is needed to treat the different file structures in CloudFoundry
try:
    from backend.services.sfsf_api import (
        get_random_user, 
        get_single_user,
        get_users,
        create_user
    )
    from backend.app.schemas import UserPublic, UserList, UserSchema, UpsertResponse
except ModuleNotFoundError:
    from services.sfsf_api import (
        get_random_user, 
        get_single_user,
        get_users,
        create_user
    )
    from app.schemas import UserPublic, UserList, UserSchema, UpsertResponse


router = APIRouter(prefix = '/users', tags = ['Users'])


@router.get("/random-user",status_code=HTTPStatus.OK, response_model=UserPublic)
def get_user():
    """
        This toy endpoint simply queries the user table with no filters and at the end apply top=1
        This is not useful for day to day but is already a good example to show how the users will return in the other API calls
    """
    raw = get_random_user()
    data = json.loads(raw) if isinstance(raw, str) else raw
    user = data['d']['results'][0]
    response = UserPublic.model_validate(user)
    return response


@router.get('/{username}', response_model=UserPublic, status_code=HTTPStatus.OK)
def read_user(username:str):
    """
        This route implement the logic for you to read a single user from SFSF
        username: provide the username which you want to return
    """
    raw = get_single_user(username)
    data = json.loads(raw) if isinstance(raw, str) else raw
    user = data['d']['results'][0]
    response = UserPublic.model_validate(user)
    return response


@router.get('/{filter}/{pageSize}', response_model=UserList, status_code=HTTPStatus.OK)
def read_users(filter:str, pageSize:int= 1000):
    """
        This API receives 2 parameters the filter query and the page size.
        filter: this parameter defines based on what your results will return for example division eq 'Manufacturing (MANU)'
        Notes: sent the filter exactly how you would be doing directly from SFSF odata API

        pageSize: allows you to define a custom page size incase you want this API cal get smaler pages from SFSF.
        Note: the pagesize will NOT interfeere on the final result you see in swager, there you'll still get the full list,
        but setting it may make SFSF to respond faster to this API by defining smaler pages
    """
    response = get_users(filter=filter, page_size=pageSize)
    result = [UserPublic.model_validate(user) for user in response]
    return {'users': result}

@router.post('/', status_code=HTTPStatus.CREATED, response_model=UpsertResponse)
def post_user_to_create(user:UserSchema):
    """
        This api receives an object of type UserSchema which is then formated to the correct upsert body format
        After that it will peform the operation and return the logs for you. 
    """
    payload = user.model_dump(by_alias=True, exclude_none=True)
    payload_json = json.dumps(payload, ensure_ascii=False)
    raw = create_user(payload_json)
    item = raw['response']['d'][0]
    result = UpsertResponse.model_validate(item)
    return result
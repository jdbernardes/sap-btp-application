from http import HTTPStatus
from fastapi import APIRouter
from ..app.schemas import Message

router = APIRouter(prefix='/root', tags=['Root'])

@router.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def hello():
    return {'message': 'Hello CF API'}

@router.get('/health', status_code=HTTPStatus.OK, response_model=Message)
async def health():
    return {'message': 'CF API online'}
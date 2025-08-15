from pydantic import BaseModel
from typing import List


class Message(BaseModel):
    message: str

class User(BaseModel):
    userID: str
    userName: str
    firstName: str
    lastName: str

class UserList(BaseModel):
    users: List[User]

from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import List


class Message(BaseModel):
    message: str

class UserPublic(BaseModel):
    userId: str
    username: str
    firstName: str
    lastName: str
    displayName: str
    email: EmailStr
    location: str
    division: str
    department: str

class UserList(BaseModel):
    users: List[UserPublic]

class MetaData(BaseModel):
    uri:str
    type:str

class UserSchema(BaseModel):
    metadata: MetaData = Field(alias='__metadata')
    userId: str
    username: str
    assignmentIdExternal: str
    status: str
    password: str
    firstName: str
    lastName: str
    email: EmailStr

    model_config = ConfigDict(populate_by_name=True)


class UpsertResponse(BaseModel):
    key: str | None = None
    status: str
    editStatus: str
    message: str
    index: int
    httpCode: int
    inlineResults: str | None = None

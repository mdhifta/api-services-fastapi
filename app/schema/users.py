from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class UserSchema(BaseModel):
    user_id: Optional[int]=None
    fname: Optional[str]=None
    lname: Optional[str]=None
    phone_number = Optional[str]=None
    email = Optional[str]=None
    password = Optional[str]=None
    roles = Optional[int]=None

    class Config:
        orm_mode = True

class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code: int
    status: bool
    message: str
    data: Optional[T]

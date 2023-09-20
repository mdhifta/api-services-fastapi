from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

class UserSignIn(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None

    class Config:
        orm_mode = True
        
class UserSignUp(BaseModel):
    fullname: Optional[str]=None
    phone_number: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None

    class Config:
        orm_mode = True

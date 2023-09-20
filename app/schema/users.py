from typing import Optional
from pydantic import BaseModel

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

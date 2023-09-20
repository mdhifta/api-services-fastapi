from fastapi import APIRouter, Depends
from app.schema.users import UserSignUp, UserSignIn
from app.core.config import connection
from sqlalchemy.orm import Session
from app.crud.users import createUser, signIn
from passlib.context import CryptContext

pwdHash = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter()

@router.post("/sign-in")
def services(user: UserSignIn, session: Session = Depends(connection)):  
    # verify user email
    result = signIn(session, user.email)
    if result == None:
        return {
            "code": 404,
            "status": False,
            "message": "Upps.. your email not found!",
            "data": None,
        }
    
    # verify password true or false 
    auth = pwdHash.verify(user.password, result.password)
    if auth:
        return {
            "code": 200,
            "status": True,
            "message": "Success login to apps.",
            "data": result,
        }
    else:
        return {
            "code": 404,
            "status": False,
            "message": "Upps.. your password wrong!",
            "data": None,
        }

@router.post("/sign-up")
def services(user: UserSignUp, session: Session = Depends(connection)):
    try:
        result = createUser(session, user)
        return {
            "code": 200,
            "status": True,
            "message": "Success to create users.",
            "data": result,
        }
    except:
        return {
            "code": 404,
            "status": False,
            "message": "Uppss.. failed to create users",
            "data": None,
        }
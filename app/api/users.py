from fastapi import APIRouter
from app.schema.users import welcome

router = APIRouter()

@router.get("/welcome")
def dashboard():
    message = welcome("peng")
    return {"ping": message}
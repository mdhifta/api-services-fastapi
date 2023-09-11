from fastapi import APIRouter
from app.schema.users import welcome

router = APIRouter()

@router.get("/api/welcome")
def dashboard():
    message = welcome()
    return {"ping": message}
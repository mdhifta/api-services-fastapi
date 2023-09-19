from fastapi import APIRouter
from app.utils.message import getMessage

router = APIRouter()

@router.get("/services")
def services():
    message = getMessage("Services Working...")

    return {
        "code": 200,
        "status": True,
        "message": message,
        "data": {
            "access": True,
        },
    }
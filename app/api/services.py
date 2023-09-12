from fastapi import APIRouter
from app.schema.message import getMessage

router = APIRouter()

@router.get("/services")
def services():
    message = getMessage("Yeay, your fastfest template working")
    
    return {
        "code": 200,
        "status": True,
        "message": message,
        "data": {
            "access": True,
        },
    }
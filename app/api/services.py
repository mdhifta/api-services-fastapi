from fastapi import APIRouter

router = APIRouter()

@router.get("/services")
def services():
    return {
        "code": 200,
        "status": True,
        "message": "Services Working...",
        "data": {
            "access": True,
        },
    }
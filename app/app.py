from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from app.core.config import Base, engine

# add flow route from api
from app.api import services
from app.api import authentication

# connection database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# base url access
@app.get("/", tags=['Index'])
async def root() -> dict:
     return {
        "code": 200,
        "status": True,
        "message": "Yeay, your fastfest template working",
        "data": {
            "access": True,
        },
    }

# if you want add new router class, just copy and edit tags name
app.include_router(services.router, tags=["Services"], prefix="/api")
app.include_router(authentication.router, tags=["Users"], prefix="/api")

# swagger modification, change if you want
def swagger():
    app.openapi_schema = get_openapi(
        title="FastFest Template",
        version="FastAPI",
        description="Build with python 3.8.10 by mdhifta",
        routes=app.routes,
    )
    
    return app.openapi_schema

app.openapi = swagger
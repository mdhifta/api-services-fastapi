from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

# add flow route from api
from .api import services

app = FastAPI()

# base url access
@app.get("/", tags=['Index'])
async def root() -> dict:
    return {"ping":"pong"}

# if you want add new router class, just copy and edit tags name
app.include_router(services.router, tags=["Services"], prefix="/api")


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
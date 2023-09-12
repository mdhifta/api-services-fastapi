from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

from .api import services

app = FastAPI(title='FastFest Template', summary='Template FastAPI by mdhifta', description="build with python 3.8.10")

# base url access
@app.get("/", tags=['Index'])
async def root() -> dict:
    return {"ping":"pong"}

# if you want add new router class, just copy and edit tags name
app.include_router(services.router, tags=["Services"], prefix="/api")
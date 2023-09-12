from fastapi import FastAPI
from .api import services

app = FastAPI()

# base url access
@app.get("/", tags=['Index'])
async def root() -> dict:
    return {"ping":"pong"}

# if you want add new router class, just copy and edit tags name
app.include_router(services.router, tags=["Services"], prefix="/api")
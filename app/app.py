from fastapi import FastAPI
from .api import users

app = FastAPI()

@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping":"Pong"}

app.include_router(users.router, tags=["Dashboard"], prefix="")
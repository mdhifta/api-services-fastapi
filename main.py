import uvicorn
from starlette.config import Config

try:
    config = Config(".env")
    if __name__ == "__main__":
      uvicorn.run("app.app:app", host=config("HOST_APP", default=None), port=int(config("PORT_APP", default=None)), reload=True)
except:
    print("Upps.. .env not found.")

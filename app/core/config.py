from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import PostgresDsn
from starlette.config import Config

config = Config(".env")

DB_DRIVER = config("DB_DRIVER", default="")
DB_USERNAME = config("DB_USERNAME", default="")
DB_PASSWORD = config("DB_PASSWORD", default="")
DB_SERVER = config("DB_SERVER", default="")
DB_PORT = config("DB_PORT", default="")
DB_NAME = config("DB_NAME", default="")
DB_SCHEMA = config("DB_SCHEME", default="")

DATABASE_URL = PostgresDsn.build(
    scheme=DB_SCHEMA,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    host=f"{DB_SERVER}:{DB_PORT}",
    path=f"/{DB_NAME}",
)

engine = create_engine(DATABASE_URL, pool_size=50, max_overflow=0)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def connection():
    connect = sessionLocal()
    try:
        yield connect
    finally:
        connect.close()
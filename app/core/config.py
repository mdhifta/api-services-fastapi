from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import PostgresDsn
from starlette.config import Config

try:
    config = Config("../../.env")

    DB_DRIVER = config("DB_DRIVER", default=None)
    DB_USERNAME = config("DB_USERNAME", default=None)
    DB_PASSWORD = config("DB_PASSWORD", default=None)
    DB_SERVER = config("DB_SERVER", default=None)
    DB_PORT = config("DB_PORT", default=None)
    DB_NAME = config("DB_NAME", default=None)
    DATABASE_URL = PostgresDsn.build(
        scheme=config("DB_SCHEME", default=None),
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=f"{DB_SERVER}:{DB_PORT}",
        path=f"/{DB_NAME}",
    )

    engine = create_engine(DATABASE_URL, pool_size=50, max_overflow=0)

    try:
        engine.connect()
        sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base = declarative_base()
    except:
        print("Upps.. your connection database error.")
except:
    print("Upps.. .env not found.")
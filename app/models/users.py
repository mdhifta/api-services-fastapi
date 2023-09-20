from sqlalchemy import Column, Integer, String
from app.core.config import Base

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    fullname = Column(String)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    roles = Column(Integer)
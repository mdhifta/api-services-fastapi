from sqlalchemy import Column, Integer, String
from core.config import Base

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    fullname = Column(String)
    phone_number = Column(String)
    email = Column(String)
    password = Column(String)
    roles = Column(Integer)
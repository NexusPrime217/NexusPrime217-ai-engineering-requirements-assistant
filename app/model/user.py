from sqlalchemy import Column, Integer, String, Enum
from app.schemas import Roles
from app.database.database import Base

class User(Base):

    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    role = Column(Enum(Roles),nullable=False)
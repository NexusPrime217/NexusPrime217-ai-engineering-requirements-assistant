from sqlalchemy import Column, Integer, String, Enum
from app.schemas import Roles
from app.database.database import Base
from datetime import datetime

class User(Base):

    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    created_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    role = Column(Enum(Roles),nullable=False, default=Roles.USER)

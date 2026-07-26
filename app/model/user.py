from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from app.schemas import Roles
from app.database.database import Base
from datetime import datetime, timezone


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    created_at = Column(DateTime(timezone=True),
                        default=lambda : datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True),
                        default=lambda : datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc))
    role = Column(Enum(Roles),nullable=False, default=Roles.USER)

    documents = relationship(
        "Document",
        back_populates="uploader"

    )

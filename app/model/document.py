from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database.database import Base

class Document(Base):

    __tablename__="document"

    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String)
    stored_filename = Column(String)
    file_size = Column(Integer)
    storage_path = Column(String)
    created_at = Column(DateTime(timezone=True), default=lambda : datetime.now(timezone.utc))

    uploaded_by = Column(Integer,
                         ForeignKey("user.id"),
                         nullable=False)
    uploader = relationship(
        "User",
        back_populates="documents")

from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.sql import func
from app.db.base_class import Base

class Message(Base):
    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("match.id"), nullable=False)
    sender_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

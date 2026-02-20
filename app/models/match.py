from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db.base_class import Base

class Match(Base):
    id = Column(Integer, primary_key=True, index=True)
    user1_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user2_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

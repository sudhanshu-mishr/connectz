from sqlalchemy import Column, Integer, ForeignKey, Boolean
from app.db.base_class import Base

class Swipe(Base):
    id = Column(Integer, primary_key=True, index=True)
    liker_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    likee_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    is_like = Column(Boolean, nullable=False)

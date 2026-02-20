from pydantic import BaseModel
from datetime import datetime

class MessageBase(BaseModel):
    match_id: int
    content: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    sender_id: int
    created_at: datetime

    class Config:
        from_attributes = True

from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)

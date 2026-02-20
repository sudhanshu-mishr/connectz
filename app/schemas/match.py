from pydantic import BaseModel, ConfigDict
from datetime import datetime

class MatchBase(BaseModel):
    user1_id: int
    user2_id: int

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

from pydantic import BaseModel, ConfigDict

class SwipeBase(BaseModel):
    likee_id: int
    is_like: bool

class SwipeCreate(SwipeBase):
    pass

class Swipe(SwipeBase):
    id: int
    liker_id: int

    model_config = ConfigDict(from_attributes=True)

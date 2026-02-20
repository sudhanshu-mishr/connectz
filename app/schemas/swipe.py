from pydantic import BaseModel

class SwipeBase(BaseModel):
    likee_id: int
    is_like: bool

class SwipeCreate(SwipeBase):
    pass

class Swipe(SwipeBase):
    id: int
    liker_id: int

    class Config:
        from_attributes = True

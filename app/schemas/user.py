from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    age: Optional[int] = None
    bio: Optional[str] = None
    photo_url: Optional[str] = None
    location_lat: Optional[float] = None
    location_lng: Optional[float] = None

class UserCreate(UserBase):
    email: EmailStr
    password: str
    full_name: str
    age: int

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDBBase(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class User(UserInDBBase):
    pass

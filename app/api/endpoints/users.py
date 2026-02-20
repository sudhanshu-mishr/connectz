from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.session import get_db
from app.crud import user as crud_user
from app.schemas.user import User, UserCreate, UserUpdate
from app.models.user import User as UserModel
from app.api import deps
from app.core import security

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(
    *,
    db: AsyncSession = Depends(get_db),
    user_in: UserCreate,
) -> Any:
    user = await crud_user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = UserModel(
        email=user_in.email,
        hashed_password=security.get_password_hash(user_in.password),
        full_name=user_in.full_name,
        age=user_in.age,
        bio=user_in.bio,
        photo_url=user_in.photo_url,
        location_lat=user_in.location_lat,
        location_lng=user_in.location_lng
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router.get("/me", response_model=User)
async def read_users_me(
    current_user: UserModel = Depends(deps.get_current_user),
) -> Any:
    return current_user

@router.put("/me", response_model=User)
async def update_user_me(
    *,
    db: AsyncSession = Depends(get_db),
    user_in: UserUpdate,
    current_user: UserModel = Depends(deps.get_current_user),
) -> Any:
    if user_in.password:
        current_user.hashed_password = security.get_password_hash(user_in.password)
    if user_in.full_name:
        current_user.full_name = user_in.full_name
    if user_in.age:
        current_user.age = user_in.age
    if user_in.bio:
        current_user.bio = user_in.bio
    if user_in.photo_url:
        current_user.photo_url = user_in.photo_url
    if user_in.location_lat:
        current_user.location_lat = user_in.location_lat
    if user_in.location_lng:
        current_user.location_lng = user_in.location_lng

    db.add(current_user)
    await db.commit()
    await db.refresh(current_user)
    return current_user

from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, not_
from app.db.session import get_db
from app.models.user import User
from app.models.swipe import Swipe
from app.models.match import Match
from app.schemas.swipe import SwipeCreate, Swipe as SwipeSchema
from app.schemas.user import User as UserSchema
from app.api import deps

router = APIRouter()

@router.get("/candidates", response_model=List[UserSchema])
async def get_candidates(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_user),
    limit: int = 20,
) -> Any:
    # Get IDs of users already swiped by current user
    swiped_ids_query = select(Swipe.likee_id).filter(Swipe.liker_id == current_user.id)
    swiped_ids_result = await db.execute(swiped_ids_query)
    swiped_ids = swiped_ids_result.scalars().all()

    # Query users not swiped and not current user
    query = select(User).filter(
        and_(
            User.id != current_user.id,
            not_(User.id.in_(swiped_ids))
        )
    ).limit(limit)

    result = await db.execute(query)
    return result.scalars().all()

@router.post("/", response_model=SwipeSchema)
async def swipe_user(
    *,
    db: AsyncSession = Depends(get_db),
    swipe_in: SwipeCreate,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    if swipe_in.likee_id == current_user.id:
        raise HTTPException(status_code=400, detail="Cannot swipe yourself")

    # Check if already swiped
    existing_swipe = await db.execute(
        select(Swipe).filter(
            Swipe.liker_id == current_user.id,
            Swipe.likee_id == swipe_in.likee_id
        )
    )
    if existing_swipe.scalars().first():
        raise HTTPException(status_code=400, detail="Already swiped this user")

    # Create Swipe
    swipe = Swipe(
        liker_id=current_user.id,
        likee_id=swipe_in.likee_id,
        is_like=swipe_in.is_like
    )
    db.add(swipe)

    # Check for match if it's a like
    if swipe_in.is_like:
        # Check if the other user liked current user
        other_swipe_query = select(Swipe).filter(
            Swipe.liker_id == swipe_in.likee_id,
            Swipe.likee_id == current_user.id,
            Swipe.is_like == True
        )
        other_swipe_result = await db.execute(other_swipe_query)
        other_swipe = other_swipe_result.scalars().first()

        if other_swipe:
            # Create Match
            match = Match(
                user1_id=min(current_user.id, swipe_in.likee_id),
                user2_id=max(current_user.id, swipe_in.likee_id)
            )
            db.add(match)

    await db.commit()
    await db.refresh(swipe)
    return swipe

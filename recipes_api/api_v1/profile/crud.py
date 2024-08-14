from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import result
from core.models.recipy import Recipy, Category
from core.models.user import User
from core.models.like import Like



async def get_user_likes(session: AsyncSession, user_id: int):
    stmt = select(User).options(selectinload(User.likes)).where(User.id==user_id)
    result = await session.execute(stmt)
    user = result.scalars().one_or_none()
    return user.likes
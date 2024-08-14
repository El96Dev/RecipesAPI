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


async def get_user_created_recipes(session: AsyncSession, user_id: int):
    author_stmt = select(User.email).where(User.id==user_id)
    author_result = await session.execute(author_stmt)
    author = author_result.scalars().one_or_none()

    if not author:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found!")

    recipes_stmt = select(Recipy).where(Recipy.author==author)
    recipes_result = await session.execute(recipes_stmt)
    return recipes_result.scalars().all()
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import result
from core.models.recipy import Recipy, Category
from core.models.user import User
from core.models.like import Like
from core.models.following import Following


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


async def follow_user(session: AsyncSession, user: User, user_id: int):
    db_user_stmt = select(User).where(User.id==user_id)
    db_user_result = await session.execute(db_user_stmt)
    db_user = db_user_result.scalars().one_or_none()

    if not db_user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found!")
    
    db_following_stmt = select(Following).where(Following.user_id==user.id, Following.following_id==user_id)
    db_following_result = await session.execute(db_following_stmt)
    db_following = db_following_result.scalars().one_or_none()
    
    if db_following:
        raise HTTPException(status_code=403, detail=f"You're already following user {user_id}")

    following = Following(user_id=user.id, following_id=user_id)
    session.add(following)
    await session.commit()
    return following


async def stop_following_user(session: AsyncSession, user: User, user_id: int):
    db_user_stmt = select(User).where(User.id==user_id)
    db_user_result = await session.execute(db_user_stmt)
    db_user = db_user_result.scalars().one_or_none()

    if not db_user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found!")
    
    db_following_stmt = select(Following).where(Following.user_id==user.id, Following.following_id==user_id)
    db_following_result = await session.execute(db_following_stmt)
    db_following = db_following_result.scalars().one_or_none()
    
    if not db_following:
        raise HTTPException(status_code=403, detail=f"You're not following user {user_id}")
    
    await session.delete(db_following)
    await session.commit()


async def get_user_followings(session: AsyncSession, user_id: int):
    stmt = select(User).options(selectinload(User.following)).where(User.id==user_id)
    result = await session.execute(stmt)
    user = result.scalars().one_or_none()
    return user.following


async def get_user_followers(session: AsyncSession, user_id: int):
    stmt = select(User).options(selectinload(User.followers)).where(User.id==user_id)
    result = await session.execute(stmt)
    user = result.scalars().one_or_none()
    return user.followers
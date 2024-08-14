from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import result
from core.models.recipy import Recipy, Category
from core.models.user import User
from core.models.like import Like
from .schemas import RecipyCreate, RecipyUpdate, RecipyUpdatePartial


async def get_recipes(session: AsyncSession):
    stmt = select(Recipy).order_by(Recipy.id)
    result = await session.execute(stmt)
    recipes = result.scalars().all()
    return list(recipes)


async def get_recipy_by_name_and_author(session: AsyncSession, recipy_name: str, author: str):
    stmt = select(Recipy).where(Recipy.name == recipy_name, Recipy.author == author)
    result = await session.execute(stmt)
    recipy = result.scalars().all()
    return recipy


async def get_category(session: AsyncSession, category_name: str):
    stmt = select(Category).where(Category.name == category_name)
    result = await session.execute(stmt)
    category = result.scalars().all()
    return category


async def get_recipy(session: AsyncSession, recipy_id: int):
    return await session.get(Recipy, recipy_id)


async def get_categories(session: AsyncSession):
    stmt = select(Category)
    result = await session.execute(stmt)
    categories = result.scalars().all()
    return list(categories)


async def create_recipy(session: AsyncSession, recipy_in: RecipyCreate, author: str):
    recipy = Recipy(**recipy_in.model_dump(), author=author)
    session.add(recipy)
    await session.commit()
    return recipy


async def update_recipy(session: AsyncSession, recipy: Recipy, 
                        recipy_update: RecipyUpdate | RecipyUpdatePartial, author: str,
                        partial: bool = False):
    db_recipy = await session.get(Recipy, recipy.id)
    if not db_recipy:
        raise HTTPException(status_code=404, detail=f"Recipy {recipy.name} doesn't exist!")
    elif db_recipy.author != author:
        raise HTTPException(status_code=403, detail="Only author can update recipy!")
    if not await check_category_exists(session, recipy_update.category):
        raise HTTPException(status_code=404, detail=f"Category {recipy_update.category} doesn't exist!")

    for key, value in recipy_update.model_dump(exclude_unset=partial).items():
        setattr(recipy, key, value)
    await session.commit()
    return recipy


async def delete_recipy(session: AsyncSession, recipy: Recipy):
    await session.delete(recipy)
    await session.commit()


async def check_category_exists(session: AsyncSession, category_name: str):
    query = select(Category).where(Category.name==category_name).exists()
    return await session.scalar(select(query))


async def check_if_like_exists(session: AsyncSession, user_id: int, recipy_id: int):
    query = select(Like).where(Like.user_id==user_id, Like.recipy_id==recipy_id).exists()
    return await session.scalar(select(query))


async def check_if_recipy_exists(session: AsyncSession, recipy_id: int):
    query = select(Recipy).where(Recipy.id==recipy_id).exists()
    return await session.scalar(select(query))


async def add_like(session: AsyncSession, user_id: int, recipy_id: int):
    like = Like(user_id=user_id, recipy_id=recipy_id)
    session.add(like)
    await session.commit()
    return like


async def remove_like(session: AsyncSession, like: Like):
    await session.delete(like)
    await session.commit()


async def get_like(session: AsyncSession, user_id: int, recipy_id: int):
    stmt = select(Like).where(Like.user_id==user_id, Like.recipy_id==recipy_id)
    result = await session.execute(stmt)
    like = result.scalars().one_or_none()
    return like



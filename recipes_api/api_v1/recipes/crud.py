from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import result
from core.models.recipy import Recipy, Category
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
    for key, value in recipy_update.model_dump(exclude_unset=partial).items():
        setattr(recipy, key, value)
    await session.commit()
    return recipy


async def delete_recipy(session: AsyncSession, recipy: Recipy):
    await session.delete(recipy)
    await session.commit()


from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import result
from core.models.recipy import Recipy
from .schemas import RecipyCreate, RecipyUpdate, RecipyUpdatePartial


async def get_recipes(session: AsyncSession):
    stmt = select(Recipy).order_by(Recipy.id)
    result = await session.execute(stmt)
    recipes = result.scalars().all()
    return list(recipes)


async def get_recipy(session: AsyncSession, recipy_id: int):
    return await session.get(Recipy, recipy_id)


async def create_recipy(session: AsyncSession, recipy_in: RecipyCreate):
    recipy = Recipy(**recipy_in.model_dump())
    session.add(recipy)
    await session.commit()
    return recipy


async def update_recipy(session: AsyncSession, recipy: Recipy, 
                        recipy_update: RecipyUpdate | RecipyUpdatePartial, partial: bool = False):
    for key, value in recipy_update.model_dump(exclude_unset=partial).items():
        setattr(recipy, key, value)
    await session.commit()
    return recipy


async def delete_recipy(session: AsyncSession, recipy: Recipy):
    await session.delete(recipy)
    await session.commit()
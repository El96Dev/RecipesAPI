from fastapi import HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.recipy import Recipy, Category, Cuisine
from core.models.user import User
from core.models.like import Like
from .schemas import RecipyCreate, RecipyUpdate, RecipyUpdatePartial
from dependencies.images import image_helper


async def get_recipes(session: AsyncSession):
    stmt = (
        select(Recipy).
        options(joinedload(Recipy.author)).
        order_by(Recipy.id)
    )
    result = await session.execute(stmt)
    recipes = result.scalars().all()
    return recipes


async def get_recipes_by_category(session: AsyncSession, category_name: str):
    if not await check_category_exists(session, category_name):
        raise HTTPException(
            status_code=404,
            detail=f"Category {category_name} doesn't exist!"
        )

    stmt = select(Recipy).where(Recipy.category == category_name)
    result = await session.execute(stmt)
    recipes = result.scalars().all()
    return list(recipes)


async def get_category(session: AsyncSession, category_name: str):
    stmt = select(Category).where(Category.name == category_name)
    result = await session.execute(stmt)
    category = result.scalars().all()
    return category


async def get_recipy(session: AsyncSession, recipy_id: int):
    stmt = (
        select(Recipy).
        where(Recipy.id == recipy_id).
        options(joinedload(Recipy.author))
    )
    result = await session.execute(stmt)
    recipy = result.scalars().one_or_none()
    if not recipy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Can't find recipy with id {recipy_id}"
        )
    return recipy


async def get_categories(session: AsyncSession):
    stmt = select(Category)
    result = await session.execute(stmt)
    categories = result.scalars().all()
    return list(categories)


async def get_cuisines(session: AsyncSession):
    stmt = select(Cuisine)
    result = await session.execute(stmt)
    cuisines = result.scalars().all()
    return list(cuisines)


async def create_recipy(
    session: AsyncSession,
    recipy_in: RecipyCreate,
    author_id: int
):
    recipy = Recipy(**recipy_in.model_dump(), author_id=author_id)
    try:
        session.add(recipy)
        await session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"You've already created recipy named {recipy_in.name}"
        )

    return recipy


async def update_recipy(
    session: AsyncSession,
    recipy: Recipy,
    recipy_update: RecipyUpdate | RecipyUpdatePartial,
    author_id: int,
    partial: bool = False
):
    db_recipy = await session.get(Recipy, recipy.id)
    if not db_recipy:
        raise HTTPException(
            status_code=404,
            detail=f"Recipy {recipy.name} doesn't exist!"
        )
    elif db_recipy.author_id != author_id:
        raise HTTPException(
            status_code=403,
            detail="Only author can update recipy!"
        )
    if not await check_category_exists(session, recipy_update.category):
        raise HTTPException(
            status_code=404,
            detail=f"Category {recipy_update.category} doesn't exist!"
        )

    for key, value in recipy_update.model_dump(exclude_unset=partial).items():
        setattr(recipy, key, value)
    await session.commit()
    return recipy


async def delete_recipy(session: AsyncSession, recipy: Recipy):
    await session.delete(recipy)
    await session.commit()


async def check_cuisine_exists(session: AsyncSession, cuisine_name: str):
    query = select(Cuisine).where(Cuisine.name == cuisine_name).exists()
    return await session.scalar(select(query))


async def check_category_exists(session: AsyncSession, category_name: str):
    query = select(Category).where(Category.name == category_name).exists()
    return await session.scalar(select(query))


async def check_if_like_exists(
    session: AsyncSession,
    user_id: int,
    recipy_id: int
):
    query = (
        select(Like).
        where(Like.user_id == user_id, Like.recipy_id == recipy_id).
        exists()
    )
    return await session.scalar(select(query))


async def check_if_recipy_exists(session: AsyncSession, recipy_id: int):
    query = select(Recipy).where(Recipy.id == recipy_id).exists()
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
    stmt = (
        select(Like).
        where(Like.user_id == user_id, Like.recipy_id == recipy_id)
    )
    result = await session.execute(stmt)
    like = result.scalars().one_or_none()
    return like


async def get_recipy_likes(recipy_id: int, session: AsyncSession):
    stmt = (
        select(Recipy).
        options(joinedload(Recipy.likes)).
        where(Recipy.id == recipy_id)
    )
    result = await session.execute(stmt)
    recipy = result.unique().scalars().one_or_none()
    if not recipy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipy with id {recipy_id} wasn't found!"
        )
    return list(recipy.likes)


async def set_recipy_image(
    recipy_id: int,
    recipy_image: UploadFile,
    user: User,
    session: AsyncSession
):
    stmt = select(Recipy).where(Recipy.id == recipy_id)
    result = await session.execute(stmt)
    recipy = result.scalars().one_or_none()
    if not recipy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipy with id {recipy_id} wasn't found!"
        )
    if recipy_image.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Image must be in jpeg or png format!"
        )

    if recipy.author != user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only author can set recipy image!"
        )

    if not image_helper.check_image_size(recipy_image, 150):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Image size must be less than 150Kb"
        )

    image_helper.save_image(recipy_image, str(recipy_id), "recipes")
    recipy.image_filename = (
        str(recipy_id) + "." + recipy_image.content_type.split("/")[-1]
    )
    await session.commit()


async def get_recipy_image(recipy_id: int, session: AsyncSession):
    query = select(Recipy).where(Recipy.id == recipy_id).exists()
    if not await session.scalar(select(query)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipy with id {recipy_id} wasn't found!"
        )

    return FileResponse(
        image_helper.get_image_filepath(str(recipy_id), "recipes")
    )

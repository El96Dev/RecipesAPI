from fastapi import HTTPException, status, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.recipy import Recipy
from core.models.user import User
from core.models.following import Following
from dependencies.images import image_helper


async def get_user_likes(session: AsyncSession, user_id: int):
    stmt = (
        select(User).
        options(selectinload(User.likes)).
        where(User.id == user_id)
    )
    result = await session.execute(stmt)
    user = result.scalars().one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} wasn't found!"
        )
    return user.likes


async def get_user_created_recipes(session: AsyncSession, user_id: int):
    stmt = select(Recipy).where(Recipy.author_id == user_id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def follow_user(session: AsyncSession, user: User, user_id: int):
    db_user_stmt = select(User).where(User.id == user_id)
    db_user_result = await session.execute(db_user_stmt)
    db_user = db_user_result.scalars().one_or_none()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail=f"User with id {user_id} not found!"
        )

    db_following_stmt = (
        select(Following).
        where(Following.user_id == user.id, Following.following_id == user_id)
    )
    db_following_result = await session.execute(db_following_stmt)
    db_following = db_following_result.scalars().one_or_none()

    if db_following:
        raise HTTPException(
            status_code=403,
            detail=f"You're already following user {user_id}"
        )

    following = Following(user_id=user.id, following_id=user_id)
    session.add(following)
    await session.commit()
    return following


async def stop_following_user(session: AsyncSession, user: User, user_id: int):
    db_user_stmt = select(User).where(User.id == user_id)
    db_user_result = await session.execute(db_user_stmt)
    db_user = db_user_result.scalars().one_or_none()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail=f"User with id {user_id} not found!"
        )

    db_following_stmt = (
        select(Following).
        where(Following.user_id == user.id, Following.following_id == user_id)
    )
    db_following_result = await session.execute(db_following_stmt)
    db_following = db_following_result.scalars().one_or_none()

    if not db_following:
        raise HTTPException(
            status_code=403,
            detail=f"You're not following user {user_id}"
        )

    await session.delete(db_following)
    await session.commit()


async def get_user_followings(session: AsyncSession, user_id: int):
    stmt = (
        select(User).
        options(selectinload(User.following)).
        where(User.id == user_id)
    )
    result = await session.execute(stmt)
    user = result.scalars().one_or_none()
    return user.following


async def get_user_followers(session: AsyncSession, user_id: int):
    stmt = (
        select(User).
        options(selectinload(User.followers)).
        where(User.id == user_id)
    )
    result = await session.execute(stmt)
    user = result.scalars().one_or_none()
    return user.followers


async def get_user_avatar(user_id: int, session: AsyncSession):
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)
    user = result.scalars().one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} wasn't found!"
        )

    return (
        FileResponse(image_helper.get_image_filepath(str(user_id), "users"))
    )


async def set_user_avatar(
    user: User,
    avatar: UploadFile,
    session: AsyncSession
):
    if avatar.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Image must be in jpeg or png format!"
        )

    if not image_helper.check_image_size(avatar, 150):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Image size must be less than 150Kb"
        )

    image_helper.save_image(avatar, str(user.id), "users")
    User.avatar_filename = (
        str(user.id) + "." + avatar.content_type.split("/")[-1]
    )
    await session.commit()

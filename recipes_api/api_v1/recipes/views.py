from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud 
from .schemas import Recipy, RecipyCreate, RecipyUpdate, RecipyUpdatePartial, Category, Like
from .dependencies import recipy_by_id, get_recipy_if_user_is_author
from core.models import db_helper
from core.models import User
from dependencies.authentication.fastapi_users import current_active_user


router = APIRouter(tags=["Recipes"])

@router.get("", response_model=list[Recipy])
async def get_recipes(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_recipes(session=session)


@router.get("/create_recipy", response_model=list[Category])
async def get_recipy_categories(session: AsyncSession = Depends(db_helper.scoped_session_dependency),
                                user: User = Depends(current_active_user)):
    return await crud.get_categories(session=session)


@router.get("/{recipy_id}", response_model=Recipy)
async def get_recipy(recipy: Recipy = Depends(recipy_by_id)):
    return recipy 


@router.post("/create_recipy", response_model=Recipy, status_code=status.HTTP_201_CREATED)
async def create_recipy(recipy_in: RecipyCreate, session: AsyncSession = Depends(db_helper.scoped_session_dependency),
                        user: User = Depends(current_active_user)):
    if not await crud.check_category_exists(session, recipy_in.category):
        raise HTTPException(status_code=422, detail=f"Category {recipy_in.category} doesn't exist!")
    if await crud.get_recipy_by_name_and_author(session=session, recipy_name=recipy_in.name, author=user.email):
        raise HTTPException(status_code=403, detail=f"Recipy {recipy_in.name} already exists!")
    else:
        return await crud.create_recipy(session=session, recipy_in=recipy_in, author = user.email)


@router.put("/{recipy_id}", response_model=Recipy)
async def update_recipy(
    recipy_update: RecipyUpdate,
    recipy: Recipy = Depends(recipy_by_id), 
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    user: User = Depends(current_active_user)):

    return await crud.update_recipy(
        session=session,
        recipy=recipy,
        recipy_update=recipy_update,
        author=user.email
    )


@router.patch("/{recipy_id}", response_model=Recipy)
async def update_recipy_partial(
    recipy_update: RecipyUpdatePartial,
    recipy: Recipy = Depends(recipy_by_id), 
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    user: User = Depends(current_active_user)):

    return await crud.update_recipy(
        session=session,
        recipy=recipy,
        recipy_update=recipy_update,
        author=user.email,
        partial=True
    )


@router.delete("/{recipy_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_recipy(recipy_id: int, 
                        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
                        user: User = Depends(current_active_user)):
    recipy = await get_recipy_if_user_is_author(recipy_id=recipy_id, author=user.email, session=session)
    await crud.delete_recipy(session=session, recipy=recipy)


@router.post("/{recipy_id}/like", status_code=status.HTTP_201_CREATED)
async def add_like(recipy_id: int, 
                   user: User = Depends(current_active_user), 
                   session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    if await crud.check_if_like_exists(session=session, user_id=user.id, recipy_id=recipy_id):
        raise HTTPException(status_code=403, detail="Like already exists!")
    elif not await crud.check_if_recipy_exists(session=session, recipy_id=recipy_id):
        raise HTTPException(status_code=404, detail=f"Recipe with id {recipy_id} doesn't exist!")
    return await crud.add_like(session=session, user_id=user.id, recipy_id=recipy_id)


@router.delete("/{recipy_id}/like", status_code=status.HTTP_204_NO_CONTENT)
async def delete_like(recipy_id: int,
                      user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    if not await crud.check_if_like_exists(session=session, user_id=user.id, recipy_id=recipy_id):
        raise HTTPException(status_code=404, detail="Like doesn't exits!")
    like = await crud.get_like(session=session, user_id=user.id, recipy_id=recipy_id)
    return await crud.remove_like(session=session, like=like)



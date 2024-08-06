from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud 
from .schemas import Recipy, RecipyCreate, RecipyUpdate, RecipyUpdatePartial
from .dependencies import recipy_by_id
from core.models import db_helper


router = APIRouter(tags=["Recipes"])

@router.get("", response_model=list[Recipy])
async def get_recipes(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_recipes(session=session)


@router.get("/{recipy_id}", response_model=Recipy)
async def get_recipy(recipy: Recipy = Depends(recipy_by_id)):
    return recipy 


@router.post("", response_model=Recipy, status_code=status.HTTP_201_CREATED)
async def create_recipy(recipy_in: RecipyCreate, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.create_recipy(session=session, recipy_in=recipy_in)


@router.put("/{recipy_id}", response_model=Recipy)
async def update_recipy(
    recipy_update: RecipyUpdate,
    recipy: Recipy = Depends(recipy_by_id), 
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_recipy(
        session=session,
        recipy=recipy,
        recipy_update=recipy_update
    )


@router.patch("/{recipy_id}", response_model=Recipy)
async def update_recipy_partial(
    recipy_update: RecipyUpdatePartial,
    recipy: Recipy = Depends(recipy_by_id), 
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_recipy(
        session=session,
        recipy=recipy,
        recipy_update=recipy_update,
        partial=True
    )


@router.delete("/{recipy_id}")
async def delete_recipy(recipy: Recipy = Depends(recipy_by_id), session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    pass
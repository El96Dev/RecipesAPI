from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud 
from .schemas import Recipy, RecipyCreate
from core.models import db_helper


router = APIRouter(tags=["Recipes"])

@router.get("", response_model=list[Recipy])
async def get_recipes(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_recipes(session=session)


@router.get("/{recipy_id}", response_model=Recipy)
async def get_recipy(recipy_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    recipy = await crud.get_recipy(session=session, recipy_id=recipy_id)
    if recipy is not None:
        return recipy
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipy {recipy_id} not found!"
        )


@router.post("", response_model=Recipy)
async def create_recipy(recipy_in: RecipyCreate, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.create_recipy(session=session, recipy_in=recipy_in)
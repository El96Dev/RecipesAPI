from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud 
from .schemas import Recipy, RecipyCreate
from .dependencies import recipy_by_id
from core.models import db_helper


router = APIRouter(tags=["Recipes"])

@router.get("", response_model=list[Recipy])
async def get_recipes(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_recipes(session=session)


@router.get("/{recipy_id}", response_model=Recipy)
async def get_recipy(recipy: Recipy = Depends(recipy_by_id)):
    return recipy 


@router.post("", response_model=Recipy)
async def create_recipy(recipy_in: RecipyCreate, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.create_recipy(session=session, recipy_in=recipy_in)


@router.put("/{recipy_id}", response_model=Recipy)
async def update_recipy():
    pass

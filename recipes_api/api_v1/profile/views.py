from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud 
from core.models import db_helper
from core.models import User
from dependencies.authentication.fastapi_users import current_active_user


router = APIRouter(tags=["Profile"])


@router.get("/{user_id}/likes")
async def get_user_likes(user_id: int, 
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_user_likes(session, user_id)


@router.get("/{user_id}/created_recipes")
async def get_user_created_recipes(user_id: int,
                                   session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_user_created_recipes(session, user_id)
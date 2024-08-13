from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, exists
from core.models import db_helper, Recipy
from . import crud


async def recipy_by_id(recipy_id: Annotated[int, Path], session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    recipy = await crud.get_recipy(session=session, recipy_id=recipy_id)
    if recipy is not None:
        return recipy
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipy {recipy_id} not found!"
        )
    

async def get_recipy_if_user_is_author(recipy_id: Annotated[int, Path], 
                                       author: str,
                                       session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    recipy = await session.get(Recipy, recipy_id)
    if recipy is not None:
        if recipy.author == author:
            return recipy
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only author can delete recipy!")
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipy {recipy_id} not found!"
        )


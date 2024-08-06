from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
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
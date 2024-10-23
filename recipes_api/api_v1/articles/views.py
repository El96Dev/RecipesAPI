from fastapi import APIRouter, HTTPException, status, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import ArticleBase, ArticleGet
from core.models import Article
from core.models import db_helper


router = APIRouter(tags=["Articles"])


@router.get("/articles", response_model=list[ArticleGet])
async def get_articles(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_articles(session)


@router.get("/articles/{article_id}/image")
async def get_article_image(article_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    image = await crud.get_article_image(article_id, session)
    return image


@router.get("/articles/{article_id}")
async def get_article(article_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_article(article_id, session)
from fastapi import APIRouter, HTTPException, status, Depends, UploadFile
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import ArticleBase, ArticleGet, ArticleUpdate
from core.models import User
from core.models import db_helper
from dependencies.authentication.current_user import current_admin_user
from .utils import orm_to_pydantic, orm_list_to_pydantic


router = APIRouter(tags=["Articles"])


@router.get("", response_model=list[ArticleGet])
@cache(expire=(60*30))
async def get_articles(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    articles = await crud.get_articles(session)
    return orm_list_to_pydantic(articles)


@router.get("/{article_id}/image")
async def get_article_image(article_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    image = await crud.get_article_image(article_id, session)
    return image


@router.get("/{article_id}")
@cache(expire=(60*30))
async def get_article(article_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    article = await crud.get_article(article_id, session)
    return orm_to_pydantic(article)


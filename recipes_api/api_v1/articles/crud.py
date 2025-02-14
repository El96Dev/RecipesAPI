from datetime import datetime

from fastapi import HTTPException, status, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from .schemas import ArticleBase
from core.models import Article, User, ArticleView
from dependencies.images import image_helper


async def get_articles(session: AsyncSession) -> list[Article]:
    stmt = select(Article).options(joinedload(Article.views))
    result = await session.execute(stmt)
    articles = result.scalars().all()
    return articles


async def get_article(article_id: int, session: AsyncSession) -> Article:
    stmt = select(Article).where(Article.id==article_id)
    result = await session.execute(stmt)
    article = result.scalars().one_or_none()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {article_id} wasn't found!")
    return article


async def get_article_image(article_id: int, session: AsyncSession) -> FileResponse:
    query = select(Article).where(Article.id==article_id).exists()
    if not await session.scalar(select(query)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {article_id} wasn't found!")

    return FileResponse(image_helper.get_image_filepath(str(article_id), "articles"))


async def create_article(new_article: ArticleBase, 
                         admin_user: User, 
                         session: AsyncSession) -> Article:
    article = Article(**new_article.model_dump(), 
                      author_id=admin_user.id, 
                      created_at=datetime.utcnow)
    session.add(article)
    await session.commit()
    return article
from fastapi import HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models import Article
from dependencies.images import image_helper


async def get_articles(session: AsyncSession):
    stmt = select(Article)
    result = await session.execute(stmt)
    articles = result.scalars().all()
    return articles


async def get_article(article_id: int, session: AsyncSession):
    stmt = select(Article).where(Article.id == article_id)
    result = await session.execute(stmt)
    article = result.scalars().one_or_none()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {article_id} wasn't found!"
        )
    return article


async def get_article_image(article_id: int, session: AsyncSession):
    query = select(Article).where(Article.id == article_id).exists()
    if not await session.scalar(select(query)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {article_id} wasn't found!"
        )

    return FileResponse(
        image_helper.get_image_filepath(str(article_id), "articles")
    )

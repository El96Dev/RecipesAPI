from datetime import datetime

from core.models import Article, User
from dependencies.images import image_helper
from fastapi import HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from .schemas import ArticleBase, ArticleUpdate


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


async def set_article_image(article_id: int, article_image: UploadFile, session: AsyncSession):
    stmt = select(Article).where(Article.id==article_id)
    result = await session.execute(stmt)
    article = result.scalars().one_or_none()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {article_id} wasn't found!")
    if article_image.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Image must be in jpeg or png format!")

    if not image_helper.check_image_size(article_image, 150):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Image size must be less than 150Kb")

    image_helper.save_image(article_image, str(article_id), "articles")
    article.image_filename = str(article_id) + "." + article_image.content_type.split("/")[-1]
    await session.commit()


async def delete_article_image(article_id: int, session: AsyncSession):
    stmt = select(Article).where(Article.id==article_id)
    result = await session.execute(stmt)
    article = result.scalars().one_or_none()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {article_id} wasn't found!")

    article.image_filename = "default.jpg"
    image_helper.delete_image(str(article_id), "articles")
 

async def create_article(new_article: ArticleBase, 
                         admin_user: User, 
                         session: AsyncSession) -> Article:
    article = Article(**new_article.model_dump(), 
                      author_id=admin_user.id, 
                      created_at=datetime.utcnow)
    session.add(article)
    await session.commit()
    return article


async def update_article(article_id: int,
                         article_update: ArticleUpdate,
                         session: AsyncSession) -> Article:
    query = select(Article).where(Article.id==article_id)
    result = await session.execute(query)
    article = result.scalars().one_or_none()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Article with id {article_id} wasn't found!"
        )
    else:
        for key, value in article_update.model_dump(exclude_unset=True).items():
            setattr(article, key, value)
        await session.commit()
        return article


async def delete_article(article_id: int,
                         session: AsyncSession):
    query = select(Article).where(Article.id==article_id)
    result = await session.execute(query)
    article = result.scalars().one_or_none()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {article_id} wasn't found!")
    else:
        await session.delete(article)
        await session.commit()
        image_helper.delete_image(article.image_filename, "articles")
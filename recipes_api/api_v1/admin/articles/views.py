from api_v1.articles import crud
from api_v1.articles.schemas import ArticleBase, ArticleGet, ArticleUpdate
from api_v1.articles.utils import orm_list_to_pydantic, orm_to_pydantic
from core.models import User, db_helper
from dependencies.authentication.current_user import current_admin_user
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/articles", dependencies=[Depends(current_admin_user)])


@router.get("", response_model=list[ArticleGet])
async def get_articles(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    articles = await crud.get_articles(session)
    return orm_list_to_pydantic(articles)


@router.get("/{article_id}/image")
async def get_article_image(article_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    image = await crud.get_article_image(article_id, session)
    return image


@router.get("/{article_id}")
async def get_article(article_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    article = await crud.get_article(article_id, session)
    return orm_to_pydantic(article)


@router.post("")
async def post_article(article: ArticleBase, 
                       user: User = Depends(current_admin_user), 
                       session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    article = await crud.create_article(article, user, session)
    return article


@router.post("/{article_id}/image")
async def post_article_image(article_id: int, 
                             article_image: UploadFile, 
                             session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    await crud.set_article_image(article_id, article_image, session)


@router.delete("/{article_id}/image")
async def delete_article_image(article_id: int, 
                               session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    await crud.delete_article_image(article_id, session)


@router.put("/{article_id}")
async def update_article(article_id: int,
                         article_update: ArticleUpdate,
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    article = await crud.update_article(article_id, article_update, session)
    return article


@router.delete("/{article_id}")
async def delete_article(article_id: int,
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    await crud.delete_article(article_id, session)
import pytest
from fastapi import HTTPException, status

from api_v1.articles import crud


@pytest.mark.asyncio()
async def test_get_empty_articles(async_db_session):
    result = await crud.get_articles(async_db_session)
    assert result == []


@pytest.mark.asyncio()
async def test_get_nonexistent_article(async_db_session):
    with pytest.raises(HTTPException) as exc_info:
        await crud.get_article(1, async_db_session)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Article with id 1 wasn't found!"

@pytest.mark.asyncio()
async def test_get_nonexistent_article_image(async_db_session):
    with pytest.raises(HTTPException) as exc_info:
        await crud.get_article_image(1, async_db_session)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Article with id 1 wasn't found!"
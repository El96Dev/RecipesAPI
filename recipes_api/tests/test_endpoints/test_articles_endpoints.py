import pytest
import asyncio


@pytest.mark.asyncio()
async def test_get_empty_articles_list(client):
    response = await client.get("/api/v1/articles")
    assert response.status_code == 200
    assert response.json() == []
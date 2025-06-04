import pytest
import asyncio


@pytest.mark.asyncio()
async def test_example_1(client):
    print("Test event loop:", id(asyncio.get_event_loop()))
    response = await client.get("/api/v1/recipes")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio()
async def test_example_2(client):
    print("Test event loop:", id(asyncio.get_event_loop()))
    response = await client.get("/api/v1/articles")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio()
async def test_register(client):
    print("Test event loop:", id(asyncio.get_event_loop()))
    user_data = {
        "email": "user524@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "te25stuser"
    }

    response = await client.post("/api/v1/auth/register", json=user_data)
    print("Response JSON:", response.json())
    assert response.status_code == 201

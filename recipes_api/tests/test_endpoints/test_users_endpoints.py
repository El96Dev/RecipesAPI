import pytest
import asyncio


@pytest.mark.asyncio()
async def test_register_user(client):
    user_data = {
        "email": "user524@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "te25stuser"
    }

    response = await client.post("/api/v1/auth/register", json=user_data)
    assert response.status_code == 201
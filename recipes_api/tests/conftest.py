import os
from unittest.mock import AsyncMock, MagicMock

import asyncio
import pytest
import pytest_asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from httpx import ASGITransport, AsyncClient
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy.schema import DropIndex, CreateIndex

from core.models import DatabaseHelper, db_helper
from core.config import settings


@pytest.fixture(scope="session")
def event_loop():
    """Create a session-scoped event loop."""
    import asyncio
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def async_engine(event_loop):
    """Create a session-scoped async SQLAlchemy engine."""
    engine = create_async_engine(settings.db_settings.url, echo=False)
    yield engine
    engine.sync_engine.dispose()


@pytest.fixture(scope="session")
def async_session_factory(async_engine):
    """Create a session-scoped async SQLAlchemy session factory."""
    return async_sessionmaker(async_engine, expire_on_commit=False)


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(os.getenv('REDIS_URL'))
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


@pytest_asyncio.fixture(scope="function")
async def async_db_session(async_session_factory):
    async with async_session_factory() as session:
        yield session
        await session.close()


@pytest_asyncio.fixture(scope="function")
async def client(async_db_session):
    from main import app
    app.dependency_overrides[db_helper.scoped_session_dependency] = lambda: async_db_session
    async with lifespan(app):
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://0.0.0.0:8000"
        ) as ac:
            yield ac


@pytest_asyncio.fixture(scope="function", autouse=True)
async def clear_database(async_db_session):
    yield
    metadata = MetaData()
    async with async_db_session.bind.connect() as conn:
        await conn.run_sync(metadata.reflect)
        for table in reversed(metadata.sorted_tables):
            if table.name != "alembic_version":
                print(f"DELETE FROM TABLE {table.name}")
                await conn.execute(table.delete())

        await conn.commit()



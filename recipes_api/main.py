import os

import uvicorn
import asyncio
from contextlib import asynccontextmanager
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.backends.redis import RedisBackend
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from core.models import Base, db_helper
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(os.getenv('REDIS_URL'))
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
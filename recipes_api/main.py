import uvicorn
from contextlib import asynccontextmanager
from core.models import Base, db_helper
from fastapi import FastAPI
from core.config import settings
from profile.views import router as profile_router
from users.views import router as users_router
from recipes.views import router as recipes_router
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)
# app.include_router(profile_router, tags=["Profile"])
# app.include_router(users_router, tags=["Users"])
# app.include_router(recipes_router, tags=["Recipes"])

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
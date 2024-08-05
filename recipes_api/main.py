import uvicorn
from contextlib import asynccontextmanager
from core.models import Base, db_helper
from fastapi import FastAPI
from profile.views import router as profile_router
from users.views import router as users_router
from recipes.views import router as recipes_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(profile_router, tags=["Profile"])
app.include_router(users_router, tags=["Users"])
app.include_router(recipes_router, tags=["Recipes"])

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
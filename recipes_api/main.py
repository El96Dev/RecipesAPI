import uvicorn
from fastapi import FastAPI
from profile.views import router as profile_router
from users.views import router as users_router
from recipes.views import router as recipes_router


app = FastAPI()
app.include_router(profile_router, tags=["Profile"])
app.include_router(users_router, tags=["Users"])
app.include_router(recipes_router, tags=["Recipes"])

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
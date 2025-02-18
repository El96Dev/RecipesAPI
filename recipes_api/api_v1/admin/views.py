from fastapi import APIRouter

from .articles.views import router as articles_router
from .forums.views import router as forums_router
from .recipes.views import router as recipes_router
from .users.views import router as users_router


router = APIRouter(tags=["Admin"])
router.include_router(articles_router, prefix="/articles")
router.include_router(forums_router, prefix="/forums")
router.include_router(recipes_router, prefix="/recipes")
router.include_router(users_router, prefix="/users")
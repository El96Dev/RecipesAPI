from fastapi import APIRouter

from .recipes.views import router as recipes_router
from .articles.views import router as articles_router
from .forums.views import router as forums_router
from .profile.views import router as profile_router
from .auth import router as auth_router
from .users import router as users_router
from .admin import admin_router


router = APIRouter()
router.include_router(recipes_router, prefix="/recipes")
router.include_router(articles_router, prefix="/articles")
router.include_router(auth_router)
router.include_router(users_router)
router.include_router(forums_router, prefix="/forums")
router.include_router(profile_router, prefix="/profile")
router.include_router(admin_router, prefix="/admin")
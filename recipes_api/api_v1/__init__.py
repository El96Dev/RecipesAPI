from fastapi import APIRouter

from .recipes.views import router as recipes_router
from .auth import router as auth_router
from .users import router as users_router


router = APIRouter()
router.include_router(recipes_router, prefix="/recipes")
router.include_router(auth_router)
router.include_router(users_router)
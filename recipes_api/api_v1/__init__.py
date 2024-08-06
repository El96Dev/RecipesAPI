from fastapi import APIRouter

from .recipes.views import router as recipes_router

router = APIRouter()
router.include_router(recipes_router, prefix="/recipes")
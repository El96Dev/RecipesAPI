from fastapi import APIRouter

from dependencies.authentication.current_user import fastapi_users
from core.schemas.user import UserRead, UserUpdate


router = APIRouter(prefix="/users", tags=["Users"])

router.include_router(
    router=fastapi_users.get_users_router(UserRead, UserUpdate)
)
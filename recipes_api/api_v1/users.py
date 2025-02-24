from core.schemas.user import UserRead, UserUpdate
from dependencies.authentication.current_user import fastapi_users
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

router.include_router(
    router=fastapi_users.get_users_router(UserRead, UserUpdate)
)
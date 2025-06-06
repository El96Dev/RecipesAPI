from fastapi import APIRouter

from dependencies.authentication.current_user import fastapi_users
from dependencies.authentication.backend import authentication_backend

from core.schemas.user import UserRead, UserCreate


router = APIRouter(prefix="/auth", tags=["Auth"])

# /login, /logout
router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend)
)

# /register
router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate)
)

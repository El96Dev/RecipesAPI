from core.schemas.user import UserCreate, UserRead
from dependencies.authentication.backend import authentication_backend
from dependencies.authentication.current_user import fastapi_users
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

# /login, /logout
router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend)
)

# /register
router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate)
)


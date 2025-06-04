from fastapi_users import schemas

from core.types.user_id import UserIdType


class UserRead(schemas.BaseUser[UserIdType]):
    username: str


class UserCreate(schemas.BaseUserCreate):
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    pass

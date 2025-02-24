from core.types.user_id import UserIdType
from fastapi_users import schemas


class UserRead(schemas.BaseUser[UserIdType]):
    username: str


class UserCreate(schemas.BaseUserCreate):
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    pass
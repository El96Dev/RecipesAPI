from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi_users import FastAPIUsers

from core.models import User
from core.types.user_id import UserIdType
from .user_manager import get_user_manager
from .backend import authentication_backend


fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager, [authentication_backend]
)

current_active_user = fastapi_users.current_user(active=True)


async def current_admin_user(
    current_user: User = Depends(current_active_user)
) -> User:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User doesn't have admin privileges"
        )
    return current_user

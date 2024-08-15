from sqlalchemy.orm import mapped_column, Mapped, relationship
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from typing import TYPE_CHECKING
from .base import Base
from core.types.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from .recipy import Recipy


class User(Base, SQLAlchemyBaseUserTable[UserIdType]):

    id: Mapped[UserIdType] = mapped_column(primary_key=True)
    likes: Mapped[list["Recipy"]] = relationship("Recipy", secondary="likes", back_populates="likes", uselist=True)
    following = relationship("User", secondary="followings", 
                             primaryjoin=("followings.c.user_id==User.id"),
                             secondaryjoin=("followings.c.following_id==User.id"))

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase
)
from typing import TYPE_CHECKING, List
from .base import Base
from core.types.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from .recipy import Recipy
    from .article import Article


class User(Base, SQLAlchemyBaseUserTable[UserIdType]):
    id: Mapped[UserIdType] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    avatar_filename: Mapped[str] = mapped_column(insert_default="default.jpg")
    articles: Mapped[List["Article"]] = relationship(back_populates="author")
    recipes: Mapped[List["Recipy"]] = relationship(back_populates="author")
    likes: Mapped[list["Recipy"]] = relationship(
        "Recipy", secondary="likes", back_populates="likes", uselist=True
    )
    followers = relationship(
        "User", secondary="followings",
        primaryjoin=("followings.c.following_id==User.id"),
        secondaryjoin=("followings.c.user_id==User.id")
    )
    is_admin: Mapped[bool] = mapped_column(default=False, nullable=False)

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)

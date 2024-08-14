from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base
from .id_mixin import IdPkMixin

if TYPE_CHECKING:
    from .user import User


class Category(Base, IdPkMixin):
    __tablename__ = "categories"
    name: Mapped[str]


class Recipy(Base, IdPkMixin):
    __tablename__ = "recipes"
    name: Mapped[str]
    author: Mapped[str] = mapped_column(ForeignKey("users.email"))
    text: Mapped[str]
    category: Mapped[str] = mapped_column(ForeignKey("categories.name"))
    likes: Mapped[list["User"]] = relationship("User", secondary="likes", back_populates="likes", uselist=True)
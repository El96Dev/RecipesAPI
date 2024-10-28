from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, UniqueConstraint
from .base import Base
from .id_mixin import IdPkMixin

if TYPE_CHECKING:
    from .user import User


class Category(Base, IdPkMixin):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(30), unique=True)


class Cuisine(Base, IdPkMixin):
    __tablename__ = "cuisines"
    name: Mapped[str] = mapped_column(String(30), unique=True)


class Recipy(Base, IdPkMixin):
    __tablename__ = "recipes"
    name: Mapped[str] 
    image_filename: Mapped[str] = mapped_column(insert_default="default.jpg")
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="recipes")
    text: Mapped[str]
    cuisine: Mapped[str] = mapped_column(ForeignKey("cuisines.name"))
    category: Mapped[str] = mapped_column(ForeignKey("categories.name"))
    likes: Mapped[list["User"]] = relationship("User", secondary="likes", back_populates="likes", uselist=True)

    __table_args__ = (UniqueConstraint('author_id', 'name', name='uq_author_name'),)
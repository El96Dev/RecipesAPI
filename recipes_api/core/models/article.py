from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import (DateTime, ForeignKey, String, Text, UniqueConstraint,
                        func)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .id_mixin import IdPkMixin

if TYPE_CHECKING:
    from .article_view import ArticleView
    from .user import User


class Article(Base, IdPkMixin):
    __tablename__ = "articles"

    title: Mapped[str] = mapped_column(String(30))
    text: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="articles")
    views: Mapped[List["ArticleView"]] = relationship(back_populates="atricle")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    image_filename: Mapped[str] = mapped_column(insert_default="default.jpg")

    __table_args__ = (UniqueConstraint('author_id', 'title', name='uq_author_title'),)

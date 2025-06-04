from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    String,
    Text,
    DateTime,
    func,
    ForeignKey,
    UniqueConstraint
)
from datetime import datetime
from typing import List, TYPE_CHECKING

from .base import Base
from .id_mixin import IdPkMixin

if TYPE_CHECKING:
    from .user import User
    from .article_view import ArticleView


class Article(Base, IdPkMixin):
    __tablename__ = "articles"

    title: Mapped[str] = mapped_column(String(30))
    text: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="articles")
    views: Mapped[List["ArticleView"]] = relationship(back_populates="atricle")
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    image_filename: Mapped[str] = mapped_column(insert_default="default.jpg")

    __table_args__ = (
        UniqueConstraint('author_id', 'title', name='uq_author_title'),
    )

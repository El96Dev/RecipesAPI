from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime

from .base import Base
from .id_mixin import IdPkMixin

if TYPE_CHECKING:
    from .article import Article


class ArticleView(Base, IdPkMixin):
    __tablename__ = "article_views"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"))
    article: Mapped["Article"] = relationship(back_populates="views")
    viewed_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

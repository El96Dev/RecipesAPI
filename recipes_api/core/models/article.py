from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, DateTime, func
from datetime import datetime

from .base import Base
from .id_mixin import IdPkMixin


class Article(Base, IdPkMixin):
    __tablename__ = "atricles"

    title: Mapped[str] = mapped_column(String(30))
    text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    image_path: Mapped[str] = mapped_column(insert_default="default.jpg")

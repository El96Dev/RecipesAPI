from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .id_mixin import IdPkMixin

if TYPE_CHECKING:
    from .forum_thread import ForumThread
    from .user import User


class ForumMessage(Base, IdPkMixin):
    __tablename__ = "forum_messages"

    message: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship("User")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    thread_id: Mapped[int] = mapped_column(ForeignKey("forum_threads.id"))
    thread: Mapped["ForumThread"] = relationship("ForumThread", back_populates="messages")
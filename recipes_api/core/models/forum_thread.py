from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .id_mixin import IdPkMixin

if TYPE_CHECKING:
    from .forum_message import ForumMessage
    from .user import User
    

class ForumThread(Base, IdPkMixin):
    __tablename__ = "forum_threads"

    title: Mapped[str] = mapped_column(String(50))
    messages: Mapped[List["ForumMessage"]] = relationship("ForumMessage", back_populates="thread")
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship("User")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    is_approved: Mapped[bool] = mapped_column(Boolean, default=False)
    approver_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    approver: Mapped["User"] = relationship("User")
    approved_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
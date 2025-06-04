from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .base import Base
from .id_mixin import IdPkMixin


class Following(Base, IdPkMixin):
    __tablename__ = "followings"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    following_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from .base import Base
from .id_mixin import IdPkMixin


class Like(Base, IdPkMixin):
    __tablename__ = "likes"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    recipy_id: Mapped[int] = mapped_column(ForeignKey("recipes.id"))

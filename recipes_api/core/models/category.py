from sqlalchemy.orm import Mapped
from .base import Base


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str]
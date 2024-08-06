from sqlalchemy.orm import Mapped
from .base import Base


class Category(Base):
    __tablename__ = "categories"
    name: Mapped[str]


class Product(Base):
    __tablename__ = "products"
    name: Mapped[str]


class Recipy(Base):
    __tablename__ = "recipes"
    name: Mapped[str]
    author: Mapped[str]
    text: Mapped[str]
    
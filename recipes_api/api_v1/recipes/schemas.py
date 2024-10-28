from datetime import datetime
from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    id: int 
    username: str


class RecipyBase(BaseModel):
    name: str
    text: str
    category: str 
    cuisine: str


class Cuisine(BaseModel):
    id: int
    name: str


class Category(BaseModel):
    id: int
    name: str


class Recipy(RecipyBase):
    id: int
    author: User


class RecipyCreate(RecipyBase):
    pass


class RecipyUpdate(RecipyBase):
    pass


class RecipyUpdatePartial(RecipyBase):
    name: str | None = None
    text: str | None = None
    category: str | None = None


class Like(BaseModel):
    id: int
    username: str
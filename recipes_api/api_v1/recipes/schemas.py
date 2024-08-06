from pydantic import BaseModel, ConfigDict

class Category(BaseModel):
    name: str


class Product(BaseModel):
    name: str


class RecipyBase(BaseModel):
    name: str
    author: str
    text: str


class Recipy(RecipyBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class RecipyCreate(RecipyBase):
    pass
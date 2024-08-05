from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel

class Product(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(30)]


class Category(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(20)]


class Recipe(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(30)]
    text: Annotated[str, MinLen(20), MaxLen(700)]
from pydantic import BaseModel, ConfigDict



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
    model_config = ConfigDict(from_attributes=True)
    id: int
    author: str


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
    user_id: int
    recipy_id: int
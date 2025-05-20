from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    text: str


class ArticleGet(ArticleBase):
    id: int
    image_path: str

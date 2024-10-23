from pydantic import BaseModel, ValidationError, validator
from fastapi import UploadFile


class ArticleBase(BaseModel):
    title: str
    text: str


class ArticleGet(ArticleBase):
    id: int
    image_path: str

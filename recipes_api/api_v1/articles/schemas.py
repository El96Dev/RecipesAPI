from datetime import datetime

from pydantic import BaseModel, ValidationError, validator
from fastapi import UploadFile


class ArticleBase(BaseModel):
    title: str
    text: str


class ArticleGet(ArticleBase):
    id: int
    image_filename: str
    created_at: datetime
    views_count: int

    class Config:
        orm_mode = True

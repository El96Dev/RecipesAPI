from datetime import datetime

from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    text: str


class ArticleUpdate(BaseModel):
    title: str | None
    text: str | None


class ArticleGet(ArticleBase):
    id: int
    image_filename: str
    created_at: datetime
    views_count: int

    @property
    def views_count(self) -> int:
        return len(self.views)

    class Config:
        orm_mode = True

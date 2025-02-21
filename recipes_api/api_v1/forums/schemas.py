from datetime import datetime

from pydantic import BaseModel


class ForumMessageBase(BaseModel):
    message: str
    author_name: str
    created_at: datetime
    forum_id: int

    @property
    def author_name(self):
        return self.author.username


class ForumThreadBase(BaseModel):
    title: str


class ForumThreadGet(ForumThreadBase):
    author_id: int
    author_name: str
    created_at: str
    is_approved: bool
    approved_at: datetime | None
    
    @property
    def author_name(self):
        return self.author.username

    class Config:
        orm_mode = True


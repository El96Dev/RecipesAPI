from pydantic import BaseModel


class Follower(BaseModel):
    id: int
    username: str


class Following(BaseModel):
    id: int
    username: str

from pydantic import BaseModel


class Follower(BaseModel):
    email: str


class Following(BaseModel):
    email: str

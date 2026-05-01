from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    title: str
    body: str
    tags: str | None = None
    likes: int = 0
    dislikes: int = 0
    views: int = 0
    user_id: int


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: str | None = None
    body: str | None = None
    tags: str | None = None
    likes: int | None = None
    dislikes: int | None = None
    views: int | None = None
    user_id: int | None = None


class PostOut(PostBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

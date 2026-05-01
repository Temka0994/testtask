from pydantic import BaseModel, EmailStr, ConfigDict

from app.schemas.post import PostOut


class UserBase(BaseModel):
    first_name: str
    last_name: str
    maiden_name: str | None = None
    age: int
    gender: str
    email: EmailStr
    phone: str
    country: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    maiden_name: str | None = None
    age: int | None = None
    gender: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    country: str | None = None


class UserOut(UserBase):
    id: int
    posts: list[PostOut] = []

    model_config = ConfigDict(from_attributes=True)

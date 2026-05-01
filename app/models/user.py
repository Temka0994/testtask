from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.models.dependencies import Base
from app.models.id_mixin import IdMixin
from app.models.timestamp_mixin import TimestampMixin


class UserTable(IdMixin, TimestampMixin, Base):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    maiden_name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    phone: Mapped[str] = mapped_column(String(50))
    country: Mapped[str] = mapped_column(String(50))

    posts: Mapped[list["PostTable"]] = relationship(back_populates="users")

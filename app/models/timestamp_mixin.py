from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import func


class CreatedAtMixin:
    @declared_attr
    def created_at(cls) -> Mapped[datetime]:
        return mapped_column(server_default=func.now())


class TimestampMixin(CreatedAtMixin):
    @declared_attr
    def updated_at(cls) -> Mapped[datetime]:
        return mapped_column(server_default=func.now(), onupdate=func.now())

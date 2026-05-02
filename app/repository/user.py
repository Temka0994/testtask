from sqlalchemy import select, desc, asc

from fastapi_pagination.ext.sqlalchemy import paginate

from app.models import UserTable
from app.repository.base import BaseRepository


class UserRepository(BaseRepository[UserTable]):
    model = UserTable

from sqlalchemy import select, asc, desc

from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import joinedload

from app.models import PostTable, UserTable
from app.repository.base import BaseRepository


class PostRepository(BaseRepository[PostTable]):
    model = PostTable

    async def get_all_by_user(self, user_id):
        query = (
            select(self.model)
            .options(joinedload(self.model.user))
            .where(self.model.user_id == user_id)
        )
        posts = await paginate(self.session, query)
        return posts

    async def get_existing_user_ids(self) -> set[int]:
        result = await self.session.execute(select(UserTable.id))
        return set(result.scalars().all())

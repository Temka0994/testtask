from typing import Generic, TypeVar, Type

from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select, desc, asc
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    model: Type[ModelType]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self, sort_by: str | None, sort_order: str = "asc"):
        query = select(self.model)
        if sort_by and hasattr(self.model, sort_by):
            column = getattr(self.model, sort_by)
            query = query.order_by(
                desc(column) if sort_order == "desc" else asc(column)
            )
        result = await paginate(self.session, query)
        return result

    async def get_by_id(self, id: int):
        result = await self.session.execute(
            select(self.model).where(self.model.id == id)
        )
        return result.scalar_one_or_none()

    async def add(self, data: ModelType) -> ModelType:
        self.session.add(data)
        await self.session.commit()
        return data

    async def update(self, data: ModelType) -> ModelType:
        self.session.add(data)
        await self.session.commit()
        return data

    async def delete(self, data: ModelType) -> None:
        await self.session.delete(data)
        await self.session.commit()

    async def add_all(self, data: list[ModelType]) -> int:
        self.session.add_all(data)
        await self.session.commit()
        return len(data)

    async def get_all_ids(self) -> set[int]:
        result = await self.session.execute(select(self.model.id))
        return {row[0] for row in result.all()}

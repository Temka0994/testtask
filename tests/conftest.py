import asyncio

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from pydantic_core import MultiHostUrl

from app.core.settings import BaseAppSettings
from app.main import app
from app.models.dependencies import Base
from app.database.test_task_db import get_session
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


class TestPostgresSettings(BaseAppSettings):
    test_postgres_db: str
    test_postgres_user: str
    test_postgres_password: str
    test_postgres_host: str
    test_postgres_port: int

    @property
    def test_postgres_url(self) -> str:
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            username=self.test_postgres_user,
            password=self.test_postgres_password,
            host=self.test_postgres_host,
            port=self.test_postgres_port,
            path=self.test_postgres_db,
        ).unicode_string()


test_settings = TestPostgresSettings()


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def engine():
    test_engine = create_async_engine(test_settings.test_postgres_url, echo=True)

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield test_engine
    await test_engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def session_factory(engine):
    session = async_sessionmaker(engine, expire_on_commit=False)
    return session


@pytest_asyncio.fixture(scope="function")
async def db_session(session_factory):
    async with session_factory() as session:
        yield session


@pytest_asyncio.fixture(scope="function")
async def get_test_session(db_session):
    async def async_get_test_session():
        yield db_session

    app.dependency_overrides[get_session] = async_get_test_session
    yield
    app.dependency_overrides.clear()


@pytest_asyncio.fixture
async def async_client(get_test_session):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

import pytest

from app.core.database import AsyncSessionLocal, get_session
from app.core.config import settings
from main import proj_app

DATABASE_URL = settings.async_database_url


async def override_get_async_session() -> AsyncSessionLocal:
    async with AsyncSessionLocal() as session:
        yield session


@pytest.fixture(scope="function")
async def app(prepare_database):
    proj_app.dependency_overrides[get_session] = override_get_async_session
    return proj_app


# Асинхронный HTTP клиент
@pytest.fixture(scope="function")
async def client(app: proj_app) -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac



import os

from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_SERVER = os.environ.get('POSTGRES_SERVER')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_DB = os.environ.get('POSTGRES_DB')

DATABASE_URL = \
    f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

engine = AsyncEngine(create_engine(DATABASE_URL, echo=True, future=True))


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session

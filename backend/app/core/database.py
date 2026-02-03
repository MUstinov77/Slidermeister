from typing import Annotated

from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
    )

from backend.app.core.config import get_settings

settings = get_settings()

async_engine: AsyncEngine | None = None
async_session_maker: async_sessionmaker[AsyncSession] | None = None


async def init_db():
    global async_engine, async_session_maker

    if async_engine is not None:
        print("Database already initialized")

    async_engine = create_async_engine(settings.DB_URI)
    async_session_maker = async_sessionmaker(
        async_engine,
        expire_on_commit=False
    )

async def destroy_db():
    global async_engine, async_session_maker

    if async_engine and async_session_maker:
        await async_engine.dispose()
        async_engine, async_session_maker = None, None


async def get_async_session():
    if not async_session_maker:
        raise RuntimeError("Session maker is not initialized")

    with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise

async def async_session_provider(
        session: Annotated[AsyncSession, Depends(get_async_session)]
):
    return session

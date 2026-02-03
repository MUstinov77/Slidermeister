from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.core.config import Settings
from backend.app.core.database import destroy_db, init_db


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_db()
    try:
        yield
    finally:
        await destroy_db()


def create_app(settings: Settings):

    app = FastAPI(
        title=settings.TITLE,
        lifespan=lifespan
    )

    app.include_router(...)

    return app

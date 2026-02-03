from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.core.database import get_async_session
from backend.app.models.user import User
from backend.app.service.base import BaseService


def get_user_service(
        session: Annotated[AsyncSession, Depends(get_async_session)]
):
    return UserService(session, User)


class UserService(BaseService):
    pass
from typing import Annotated

from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer

from backend.app.models.user import User
from backend.app.service.auth.jwt import JWTService
from backend.app.service.user import UserService, get_user_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def authenticate_user(
        user_service: Annotated[UserService, Depends(get_user_service)],
        token: Annotated[str, Depends(oauth2_scheme)],
):
    payload = JWTService().decode_token(token)
    user_credentials = payload.get("context")
    user_id = user_credentials.get("user_id")
    user = user_service.retrieve_one(User.id, user_id)
    return user

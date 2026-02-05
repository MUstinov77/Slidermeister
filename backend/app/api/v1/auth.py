from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from backend.app.models.user import User
from backend.app.schema.auth import JWTResponse
from backend.app.schema.user import UserCreateSchema
from backend.app.service.auth.hash import Hasher
from backend.app.service.auth.jwt import JWTService
from backend.app.service.user import UserService, get_user_service


DEFAULT_TAG = "auth"

router = APIRouter(
    tags=[DEFAULT_TAG],
)


@router.post(
    "/signup",
    status_code=201
)
async def signup(
        user_create_data: UserCreateSchema,
        user_service: Annotated[UserService, Depends(get_user_service)],
):
    user_data = user_create_data.model_dump()
    password = user_data.pop("password")
    user_data["hashed_password"] = Hasher().hash_password(password)
    await user_service.create_instance(user_data)
    return {"message": "user created"}

@router.post(
    "/login",
    response_model=JWTResponse
)
async def login(
        login_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        user_service: Annotated[UserService, Depends(get_user_service)],
):
    username = login_data.username
    user = await user_service.retrieve_one(User.username, username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not Hasher().verify_password(login_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = JWTService().create_and_encode_token(user.dict())
    return {'access_token': token}


@router.get("/logout")
async def logout():
    pass
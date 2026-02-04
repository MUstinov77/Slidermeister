from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm


DEFAULT_TAG = "auth"

router = APIRouter(
    tags=[DEFAULT_TAG],
)


@router.post("/token")
async def login(
        login_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    pass


@router.get("/logout")
async def logout():
    pass
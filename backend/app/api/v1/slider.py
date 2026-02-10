from typing import Annotated

from fastapi import APIRouter, Depends

from langchain.chat_models import init_chat_model

from backend.app.service.auth.request_validator import authenticate_user
from backend.app.service.llm.llm import get_model


DEFAULT_TAG = "slides"

router = APIRouter(
    dependencies=(
        Depends(authenticate_user),
    ),
    tags=[DEFAULT_TAG],
)

# @router.post(
#     "/send"
# )
# async def send_message(
#         content: str,
#         model = Depends(get_model)
# ):
#     model = init_chat_model(
#     )
#     model.invoke()


@router.get("/")
async def get_slides():
    return {"message": "Ok"}
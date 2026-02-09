from fastapi import APIRouter


DEFAULT_TAG = "slides"

router = APIRouter(
    tags=[DEFAULT_TAG],
)

@router.post(
    "/send"
)
async def send_message():
    pass
from fastapi import APIRouter

from backend.app.api.v1 import auth

router = APIRouter(
    prefix="/v1"
)

router.include_router(
    auth.router,
    prefix="/auth"
)


@router.get(
    "/",
    tags=["Health check"]
)
async def health_check():
    return {"message": "OK"}
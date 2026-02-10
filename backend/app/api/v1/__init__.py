from fastapi import APIRouter

from backend.app.api.v1 import auth, slider

router = APIRouter(
    prefix="/v1"
)

router.include_router(
    auth.router,
    prefix="/auth"
)
router.include_router(
    slider.router,
    prefix="/slider"
)


@router.get(
    "/",
    tags=["Health check"]
)
async def health_check():
    return {"message": "OK"}
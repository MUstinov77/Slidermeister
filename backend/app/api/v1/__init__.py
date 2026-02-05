from backend.app.api.v1 import auth


from fastapi import APIRouter

router = APIRouter(
    prefix="/v1"
)

router.include_router(auth.router)

from fastapi import APIRouter


DEFAULT_TAG = "auth"

router = APIRouter(
    tags=[DEFAULT_TAG],
)


@router.post("/token")
async def login():
    pass


@router.get("/logout")
async def logout():
    pass
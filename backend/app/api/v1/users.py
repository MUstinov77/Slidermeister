from fastapi import APIRouter


DEFAULT_TAG = "users"

router = APIRouter(
    tags=[DEFAULT_TAG],
)

@router.get("/")
async def get_me():
    pass


@router.patch("/")
async def update_me():
    pass


@router.delete("/")
async def delete_me():
    pass

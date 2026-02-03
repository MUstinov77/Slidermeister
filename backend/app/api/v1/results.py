from fastapi import APIRouter


DEFAULT_TAG = "results"

router = APIRouter(
    tags=[DEFAULT_TAG],
)
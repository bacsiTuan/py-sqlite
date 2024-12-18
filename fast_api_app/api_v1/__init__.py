from fastapi import FastAPI, APIRouter

from fast_api_app.api_v1 import (
    math_ai,
)

api_router = APIRouter()
api_router.include_router(math_ai.router, tags=["math-ai"], prefix="/executor")


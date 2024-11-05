from fastapi import APIRouter

from src.api.v1.routers import auth_api, user_api

api_router = APIRouter()
api_router.include_router(user_api.router, prefix="/v1", tags=["v1"])
api_router.include_router(auth_api.router, prefix="/v1", tags=["v1"])

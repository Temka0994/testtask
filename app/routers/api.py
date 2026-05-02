from fastapi_pagination import add_pagination

from app.routers.user import router as user_router
from app.routers.post import router as post_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(user_router)
api_router.include_router(post_router)

add_pagination(api_router)

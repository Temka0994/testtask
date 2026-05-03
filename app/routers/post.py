from fastapi import APIRouter, Depends
from fastapi_pagination import Page

from app.dependencies.post import get_post_service
from app.schemas.post import PostOut, PostCreate, PostUpdate
from app.service.post import PostService

router = APIRouter(prefix="/post", tags=["Post"])


@router.get("/get_all/", response_model=Page[PostOut])
async def get_posts(
    sort_by: str | None = None,
    sort_order: str = "asc",
    service: PostService = Depends(get_post_service),
) -> Page[PostOut]:
    return await service.get_posts(sort_by=sort_by, sort_order=sort_order)


@router.get("/get_all_by_user/{user_id}/", response_model=Page[PostOut])
async def get_posts_by_user(
    user_id: int, service: PostService = Depends(get_post_service)
) -> Page[PostOut]:
    return await service.get_posts_by_user(user_id)


@router.get("/get/{post_id}", response_model=PostOut)
async def get_post_by_id(
    post_id: int, service: PostService = Depends(get_post_service)
) -> PostOut:
    return await service.get_post_by_id(post_id)


@router.post("/add/", response_model=PostOut)
async def add_post(
    data: PostCreate, service: PostService = Depends(get_post_service)
) -> PostOut:
    return await service.add_post(data)


@router.patch("/update/{post_id}", response_model=PostOut)
async def update_post(
    post_id: int, new_data: PostUpdate, service: PostService = Depends(get_post_service)
) -> PostOut:
    return await service.update_post(post_id, new_data)


@router.delete("/delete/{post_id}")
async def delete_post(
    post_id: int, service: PostService = Depends(get_post_service)
) -> int:
    return await service.delete_post(post_id)


@router.post("/import/")
async def import_posts(service: PostService = Depends(get_post_service)) -> str:
    return await service.import_posts_from_dummy()

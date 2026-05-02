from fastapi import APIRouter, Depends
from fastapi_pagination import Page

from app.dependencies.user import get_user_service
from app.schemas.user import UserOut, UserCreate, UserUpdate
from app.service.user import UserService

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/get_all/", response_model=Page[UserOut])
async def get_users(
    sort_by: str | None = None,
    sort_order: str = "asc",
    service: UserService = Depends(get_user_service),
) -> Page[UserOut]:
    return await service.get_users(sort_by=sort_by, sort_order=sort_order)


@router.get("/get/{user_id}/", response_model=UserOut)
async def get_user(
    user_id: int, service: UserService = Depends(get_user_service)
) -> UserOut:
    return await service.get_user_by_id(user_id)


@router.post("/add/", response_model=UserOut)
async def add_user(
    data: UserCreate, service: UserService = Depends(get_user_service)
) -> UserOut:
    return await service.add_user(data)


@router.patch("/update/{user_id}", response_model=UserOut)
async def update_user(
    user_id: int, data: UserUpdate, service: UserService = Depends(get_user_service)
) -> UserOut:
    return await service.update_user(user_id, data)


@router.delete("/delete/{user_id}")
async def delete_user(
    user_id: int, service: UserService = Depends(get_user_service)
) -> int:
    return await service.delete_user(user_id)


@router.post("/import/")
async def import_users(service: UserService = Depends(get_user_service)) -> str:
    return await service.import_users_from_dummy()

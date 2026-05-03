import random
import httpx
from fastapi import HTTPException
from fastapi_pagination import Page

from app.models import UserTable
from app.repository.user import UserRepository
from app.schemas.user import UserOut


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_users(
        self, sort_by: str | None, sort_order: str = "asc"
    ) -> Page[UserOut]:
        users = await self.user_repository.get_all(
            sort_by=sort_by, sort_order=sort_order
        )
        return users

    async def get_user_by_id(self, id: int) -> UserOut | None:
        user = await self.user_repository.get_by_id(id)
        return user

    async def add_user(self, data) -> UserOut:
        random_id = random.randint(10**8, 10**8 * 2)

        user = UserTable(
            id=random_id,
            first_name=data.first_name,
            last_name=data.last_name,
            maiden_name=data.maiden_name,
            age=data.age,
            gender=data.gender,
            email=data.email,
            phone=data.phone,
            country=data.country,
        )
        try:
            created_user = await self.user_repository.add(user)
            return created_user
        except Exception as e:
            print(f"An error: {e}")
            raise HTTPException(status_code=500, detail="Failed to add user.")

    async def update_user(self, id, new_data) -> UserOut:
        user = await self.user_repository.get_by_id(id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        try:
            if new_data.first_name:
                user.first_name = new_data.first_name
            if new_data.last_name:
                user.last_name = new_data.last_name
            if new_data.maiden_name:
                user.maiden_name = new_data.maiden_name
            if new_data.age:
                user.age = new_data.age
            if new_data.gender:
                user.gender = new_data.gender
            if new_data.email:
                user.email = new_data.email
            if new_data.phone:
                user.phone = new_data.phone
            if new_data.country:
                user.country = new_data.country
            updated_user = await self.user_repository.update(user)
            return updated_user
        except Exception as e:
            print(f"An error: {e}")
            raise HTTPException(status_code=500, detail="Failed to update user.")

    async def delete_user(self, id) -> int:
        user = await self.user_repository.get_by_id(id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        await self.user_repository.delete(user)
        return id

    async def import_users_from_dummy(self):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://dummyjson.com/users?limit=50")
            response.raise_for_status()
            data = response.json().get("users", [])

        existing_ids = await self.user_repository.get_all_ids()

        new_users = [
            UserTable(
                id=user["id"],
                first_name=user.get("firstName"),
                last_name=user.get("lastName"),
                maiden_name=user.get("maidenName"),
                age=user.get("age"),
                gender=user.get("gender"),
                email=user.get("email"),
                phone=user.get("phone"),
                country=user.get("address").get("country"),
            )
            for user in data
            if user["id"] not in existing_ids
        ]

        added_users = await self.user_repository.add_all(new_users)
        return f"Added {added_users} users."

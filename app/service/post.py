import httpx

from fastapi import HTTPException
from fastapi_pagination import Page

from app.models import PostTable
from app.repository.post import PostRepository
from app.schemas.post import PostOut


class PostService:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    async def get_posts(
        self, sort_by: str | None, sort_order: str = "asc"
    ) -> Page[PostOut]:
        posts = await self.post_repository.get_all(
            sort_by=sort_by, sort_order=sort_order
        )
        return posts

    async def get_posts_by_user(self, user_id: int) -> Page[PostOut]:
        posts = await self.post_repository.get_all_by_user(user_id)
        return posts

    async def get_post_by_id(self, post_id: int) -> PostOut | None:
        post = await self.post_repository.get_by_id(post_id)
        return post

    async def add_post(self, data) -> PostOut:
        post = PostTable(
            title=data.title, body=data.body, tags=data.tags, user_id=data.user_id
        )
        try:
            created_post = await self.post_repository.add(post)
            return created_post
        except Exception as e:
            print(f"An error: {e}")
            raise HTTPException(status_code=500, detail="Failed to add post.")

    async def update_post(self, post_id: int, new_data) -> PostOut:
        post = await self.post_repository.get_by_id(post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found.")
        try:
            if new_data.title:
                post.title = new_data.title
            if new_data.body:
                post.body = new_data.body
            if new_data.tags:
                post.tags = new_data.tags
            if new_data.user_id:
                post.user_id = new_data.user_id
            updated_post = await self.post_repository.update(post)
            return updated_post
        except Exception as e:
            print(f"An error: {e}")
            raise HTTPException(status_code=500, detail="Failed to update post.")

    async def delete_post(self, post_id: int) -> int:
        post = await self.post_repository.get_by_id(post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found.")
        await self.post_repository.delete(post)
        return post_id

    async def import_posts_from_dummy(self):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://dummyjson.com/posts?limit=50")
            response.raise_for_status()
            data = response.json().get("posts", [])

        existing_ids = await self.post_repository.get_all_ids()
        existing_user_ids = await self.post_repository.get_existing_user_ids()

        new_posts = [
            PostTable(
                id=post["id"],
                title=post.get("title"),
                body=post.get("body"),
                tags=",".join(post.get("tags", [])),
                likes=post.get("reactions").get("likes"),
                dislikes=post.get("reactions").get("dislikes"),
                views=post.get("views"),
                user_id=(
                    post.get("userId")
                    if post.get("userId") in existing_user_ids
                    else None
                ),
            )
            for post in data
            if post["id"] not in existing_ids
        ]

        added_posts = await self.post_repository.add_all(new_posts)
        return f"Added {added_posts} posts."

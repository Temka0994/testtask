from app.database.test_task_db import SessionDepend
from app.repository.post import PostRepository
from app.service.post import PostService


def get_post_service(db: SessionDepend):
    repository = PostRepository(db)

    return PostService(repository)

from app.database.test_task_db import SessionDepend
from app.repository.user import UserRepository
from app.service.user import UserService


def get_user_service(db: SessionDepend):
    repository = UserRepository(db)

    return UserService(repository)

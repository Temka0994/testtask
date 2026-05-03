import pytest


async def create_test_user(async_client):
    response = await async_client.post(
        "/user/add/",
        json={
            "first_name": "Test",
            "last_name": "User",
            "age": 25,
            "gender": "male",
            "email": "test@test.com",
            "phone": "123-456",
            "country": "Ukraine",
        },
    )
    return response.json()["id"]


@pytest.mark.asyncio
async def test_create_post(async_client):
    user_id = await create_test_user(async_client)
    response = await async_client.post(
        "/post/add/",
        json={
            "title": "Test Post",
            "body": "Test body",
            "user_id": user_id,
        },
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Post"


@pytest.mark.asyncio
async def test_get_posts(async_client):
    response = await async_client.get("/post/get_all/")
    assert response.status_code == 200
    assert "items" in response.json()


@pytest.mark.asyncio
async def test_get_post_not_found(async_client):
    response = await async_client.get("/post/get/8000")
    assert response.status_code == 200
    assert response.json() is None


@pytest.mark.asyncio
async def test_update_post(async_client):
    user_id = await create_test_user(async_client)
    create = await async_client.post(
        "/post/add/",
        json={
            "title": "Original",
            "body": "Body",
            "user_id": user_id,
        },
    )
    post_id = create.json()["id"]

    response = await async_client.patch(
        f"/post/update/{post_id}", json={"title": "Updated Title"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


@pytest.mark.asyncio
async def test_delete_post(async_client):
    user_id = await create_test_user(async_client)
    create = await async_client.post(
        "/post/add/",
        json={
            "title": "ToDelete",
            "body": "Body",
            "user_id": user_id,
        },
    )
    post_id = create.json()["id"]

    response = await async_client.delete(f"/post/delete/{post_id}")
    assert response.status_code == 200

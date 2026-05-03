import pytest


@pytest.mark.asyncio
async def test_create_user(async_client):
    response = await async_client.post(
        "/user/add/",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "age": 30,
            "gender": "male",
            "email": "john@test.com",
            "phone": "123-456",
            "country": "Ukraine",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"
    assert data["email"] == "john@test.com"


@pytest.mark.asyncio
async def test_get_users(async_client):
    response = await async_client.get("/user/get_all/")
    assert response.status_code == 200
    assert "items" in response.json()


@pytest.mark.asyncio
async def test_get_user_not_found(async_client):
    response = await async_client.get("/user/get/8000/")
    assert response.status_code == 200
    assert response.json() is None


@pytest.mark.asyncio
async def test_update_user(async_client):
    create = await async_client.post(
        "/user/add/",
        json={
            "first_name": "Jane",
            "last_name": "Doe",
            "age": 25,
            "gender": "female",
            "email": "jane@test.com",
            "phone": "789-012",
            "country": "Ukraine",
        },
    )
    user_id = create.json()["id"]

    response = await async_client.patch(
        f"/user/update/{user_id}", json={"first_name": "Updated"}
    )
    assert response.status_code == 200
    assert response.json()["first_name"] == "Updated"


@pytest.mark.asyncio
async def test_delete_user(async_client):
    create = await async_client.post(
        "/user/add/",
        json={
            "first_name": "ToDelete",
            "last_name": "User",
            "age": 20,
            "gender": "male",
            "email": "delete@test.com",
            "phone": "000-000",
            "country": "Ukraine",
        },
    )
    user_id = create.json()["id"]

    response = await async_client.delete(f"/user/delete/{user_id}")
    assert response.status_code == 200

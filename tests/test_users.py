from utils.api_client import APIClient


client = APIClient("https://jsonplaceholder.typicode.com")


def test_get_user_by_id():
    response = client.get("/users/1")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    assert "email" in data
    assert "company" in data


def test_get_all_users():
    response = client.get("/users")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
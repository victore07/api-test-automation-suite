from utils.api_client import APIClient


client = APIClient("https://jsonplaceholder.typicode.com")


def test_missing_user_returns_empty_object():
    response = client.get("/users/999999")

    assert response.status_code == 200

    data = response.json()
    assert data == {}


def test_missing_post_returns_empty_object():
    response = client.get("/posts/999999")

    assert response.status_code == 200
    
    data = response.json()
    assert data == {}
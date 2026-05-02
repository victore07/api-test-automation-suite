from utils.api_client import APIClient


client = APIClient("https://jsonplaceholder.typicode.com")


def test_get_all_posts():
    response = client.get("/posts")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_post_by_id():
    response = client.get("/posts/1")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "userId" in data
    assert "title" in data
    assert "body" in data
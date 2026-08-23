from fastapi.testclient import TestClient
from Main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
def test_health():
    response = client.get("/items/health")

    assert response.status_code == 200
    def test_create_item():
    response = client.post(
        "/items/",
        json={
            "name": "Phone",
            "price": 20000
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Phone"
def test_search_items():
    response = client.get("/items/search?name=Phone")

    assert response.status_code == 200
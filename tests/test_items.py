from fastapi.testclient import TestClient
from Main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
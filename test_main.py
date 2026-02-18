from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "CI/CD radi!"

def test_add():
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    assert "CI/CD Demo" in response.text


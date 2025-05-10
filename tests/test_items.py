from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_item():
    response = client.post("/items", json={"id": 1, "name": "Book", "price": 10.0, "in_stock": True})
    assert response.status_code == 200
    assert response.json()["name"] == "Book"


def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item():
    client.post("/items", json={"id": 2, "name": "Pen", "price": 2.5, "in_stock": False})
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Pen"


def test_update_item():
    client.post("/items", json={"id": 3, "name": "Pencil", "price": 1.0, "in_stock": True})
    response = client.put("/items/3", json={"id": 3, "name": "Pencil HB", "price": 1.2, "in_stock": False})
    assert response.status_code == 200
    assert response.json()["name"] == "Pencil HB"


def test_delete_item():
    client.post("/items", json={"id": 4, "name": "Eraser", "price": 0.5, "in_stock": True})
    response = client.delete("/items/4")
    assert response.status_code == 200
    assert response.json()["detail"] == "Item deleted"

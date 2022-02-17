
import fastapi
from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)
data = {
    "id":1,
    "task": "task1",
    "due_date": "12-2-22",
    "is_completed": True,
    "assigned_to": "yash",
    "group_title": "group1"
}

def test_create_todo():
    response = client.post("/api/todo/", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all_todo():
    response = client.get("/api/todo", json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_get_todo():
    response = client.get("/api/todo/1")
    assert response.status_code == 200
    assert response.json() == data

def test_update_todo():
    response = client.put("/api/todo/1/", json = {
    "id":1,
    "task": "task1",
    "due_date": "12-2-22",
    "is_completed": False,
    "assigned_to": "yashm",
    "group_title": "group1"
})
    assert response.status_code == 200
    assert response.json() == {
    "id":1,
    "task": "task1",
    "due_date": "12-2-22",
    "is_completed": False,
    "assigned_to": "yashm",
    "group_title": "group1"
}

def test_delete_todo():
    response = client.delete("/api/todo/1/")
    assert response.status_code == 200
    assert response.json() == {
    "id":1,
    "task": "task1",
    "due_date": "12-2-22",
    "is_completed": True,
    "assigned_to": "yash",
    "group_title": "group1"
}
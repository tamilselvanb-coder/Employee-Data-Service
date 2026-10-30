from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_get_employees_list():
    res = client.get("/employees")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_employee_404():
    res = client.get("/employees/Ravi")
    assert res.status_code == 404

def test_create_employee_success():
    payload = {"name": "TestUser", "department": "IT", "salary": 50000}
    res = client.post("/employees", json=payload)
    assert res.status_code == 201
    assert res.json()["name"] == "TestUser"

def test_create_employee_invalid_salary():
    payload = {"name": "TestUser", "department": "IT", "salary": -5422}
    res = client.post("/employees", json=payload)
    assert res.status_code == 422

def test_create_employee_empty_name():
    payload = {"name": "", "department": "IT", "salary": 50000}
    res = client.post("/employees", json=payload)
    assert res.status_code == 422

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


# 1. Test GET /health
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# 2. Test GET /employees (List all)
def test_get_all_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# 3. Test GET /employees/{name} - Success
def test_get_employee_success():
    response = client.get("/employees/Arun")
    assert response.status_code == 200
    assert response.json()["name"] == "Arun"


# 4. Test GET /employees/{name} - 404 Not Found
def test_get_employee_not_found():
    response = client.get("/employees/Ravi")
    assert response.status_code == 404


# 5. Test POST /employees - Invalid Salary (422 Unprocessable Entity)
def test_add_employee_invalid_salary():
    payload = {"name": "Test", "department": "IT", "salary": -5}
    response = client.post("/employees", json=payload)
    assert response.status_code == 422


# 6. Test POST /employees - Empty Name (422 Unprocessable Entity)
def test_add_employee_empty_name():
    payload = {"name": "", "department": "IT", "salary": 50000}
    response = client.post("/employees", json=payload)
    assert response.status_code == 422
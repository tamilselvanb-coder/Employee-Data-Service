import json
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Employee Data Service")

# Path to employees.json at the project root
BASE_DIR = Path(__file__).resolve().parent.parent
JSON_FILE = BASE_DIR / "employees.json"


# Pydantic schema for request validation
class EmployeeSchema(BaseModel):
    name: str = Field(
        ..., min_length=1, description="Employee name must not be empty"
    )
    department: str
    salary: float = Field(
        ..., gt=0, description="Salary must be greater than 0"
    )


# Helper function to read employees from JSON file
def load_employees() -> List[dict]:
    if not JSON_FILE.exists():
        return []
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# Helper function to write employees back to JSON file
def save_employees(data: List[dict]):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# 1. Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}


# 2. List all employees endpoint
@app.get("/employees")
def get_all_employees():
    return load_employees()


# 3. Get single employee by name endpoint (Returns 404 if not found)
@app.get("/employees/{name}")
def get_employee_by_name(name: str):
    employees = load_employees()
    for emp in employees:
        if emp["name"].lower() == name.lower():
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")


# 4. Add new employee endpoint (With Pydantic validation)
@app.post("/employees", status_code=201)
def add_employee(employee: EmployeeSchema):
    employees = load_employees()
    new_data = employee.model_dump()
    employees.append(new_data)
    save_employees(employees)
    return new_data
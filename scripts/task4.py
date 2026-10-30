import json
from pathlib import Path
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()
DATA_FILE = Path(__file__).parent.parent / "employees.json"

class EmployeeSchema(BaseModel):
    name: str = Field(..., min_length=1)
    department: str
    salary: float = Field(..., gt=0)

def load_employees():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/employees")
def get_employees():
    return load_employees()

@app.get("/employees/{name}")
def get_employee_by_name(name: str):
    employees = load_employees()
    for emp in employees:
        if emp["name"].lower() == name.lower():
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees", status_code=201)
def create_employee(emp: EmployeeSchema):
    employees = load_employees()
    new_emp = emp.model_dump()
    employees.append(new_emp)
    with open(DATA_FILE, "w") as f:
        json.dump(employees, f, indent=2)
    return new_emp
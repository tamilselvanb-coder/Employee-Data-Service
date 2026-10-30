import csv
from collections.abc import Callable
from functools import wraps
from pathlib import Path
from typing import Any

# Define base path pointing to the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


def log_call(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


def calculate_bonus(
    salary: float, rate: float = 0.1, *extras: float, **options: Any
) -> float:
    bonus = (salary * rate) + sum(extras)
    if "cap" in options:
        bonus = min(bonus, options["cap"])
    return bonus


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = float(salary)

    @property
    def annual_salary(self) -> float:
        return self.salary * 12

    def get_details(self) -> str:
        return f"{self.name} {int(self.salary)}"


class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int) -> None:
        super().__init__(name, salary)
        self.team_size = team_size

    @log_call
    def get_details(self) -> str:
        base_details = super().get_details()
        return f"{base_details}\nTeam Size: {self.team_size}"


def process_employees() -> None:
    csv_file = "C:/Users/Z40-B/Documents/Employee Data Service/scripts/employees.csv"

    with open(csv_file, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"].strip()
            salary = float(row["salary"].strip())

            print(name)
            if salary < 50000:
                print("Low Salary")
            elif salary < 70000:
                print("Medium Salary")
            else:
                print("High Salary")

    mgr = Manager("Divya", 75000, 5)
    print(mgr.get_details())


if __name__ == "__main__":
    process_employees()

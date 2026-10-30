import functools

# 1. calculate_bonus
def calculate_bonus(salary: float, rate: float = 0.1, *extras: float, **options) -> float:
    bonus = (salary * rate) + sum(extras)
    if "cap" in options:
        bonus = min(bonus, options["cap"])
    return bonus

# 2. Decorator log_call
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 3. Employee Base Class
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    @property
    def annual_salary(self) -> float:
        return self.salary * 12

    def get_details(self) -> str:
        return f"{self.name} {self.salary}"

# 4. Manager Subclass
class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int):
        super().__init__(name, salary)
        self.team_size = team_size

    @log_call
    def get_details(self) -> str:
        return f"{self.name} {self.salary}\nTeam Size: {self.team_size}"

if __name__ == "__main__":
    # Complete dataset with all 5 employees from employees.csv
    employees_data = [
        {"name": "Arun", "salary": 30000},
        {"name": "Priya", "salary": 45000},
        {"name": "Rahul", "salary": 60000},
        {"name": "Divya", "salary": 75000},
        {"name": "Karthik", "salary": 90000},
    ]

    # Salary Categorization Loop
    for emp in employees_data:
        print(emp["name"])
        salary = emp["salary"]
        if salary < 50000:
            print("Low Salary")
        elif salary < 70000:
            print("Medium Salary")
        else:
            print("High Salary")

    # Manager Output
    mgr = Manager(name="Divya", salary=75000, team_size=5)
    print(mgr.get_details())

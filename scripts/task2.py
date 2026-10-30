import csv
import json
import logging
from pathlib import Path
from typing import List, Dict, Optional, Union
import openpyxl
import fitz  # PyMuPDF

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def process_files(data_dir: Path) -> None:
    csv_file = data_dir / "employees.csv"
    json_file = data_dir / "employees.json"
    high_earners_file = data_dir / "high_earners.csv"

    # Read CSV and write JSON / High Earners
    employees: List[Dict[str, Union[str, int]]] = []
    high_earners: List[Dict[str, Union[str, int]]] = []

    with open(csv_file, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_data = {
                "name": row["name"].strip(),
                "department": row["department"].strip(),
                "salary": int(row["salary"].strip())
            }
            employees.append(row_data)
            if row_data["salary"] > 50000:
                high_earners.append(row_data)

    with open(json_file, mode="w") as f:
        json.dump(employees, f, indent=2)

    with open(high_earners_file, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "department", "salary"])
        writer.writeheader()
        writer.writerows(high_earners)

    print(f"Rows read: {len(employees)} High earners written: {len(high_earners)}")

    # Excel Operations (Excluding header in read-back row count)
    excel_file = data_dir / "salary.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["name", "department", "salary"])
    for emp in employees:
        ws.append([emp["name"], emp["department"], emp["salary"]])
    wb.save(excel_file)

    wb_read = openpyxl.load_workbook(excel_file)
    ws_read = wb_read.active
    data_rows = list(ws_read.iter_rows(min_row=2, values_only=True))
    print(f"salary.xlsx created and read back: {len(data_rows)} rows")

def read_file(file_path: Union[str, Path]) -> Optional[Dict]:
    path = Path(file_path)
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {path.name}")
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON format: {path.name}")
    return None

def find_employee(name: str, employees: List[Dict]) -> Optional[Dict]:
    for emp in employees:
        if emp.get("name") == name:
            return emp
    return None

if __name__ == "__main__":
    base_path = Path(__file__).parent.parent
    process_files(base_path)
    read_file("missing.txt")
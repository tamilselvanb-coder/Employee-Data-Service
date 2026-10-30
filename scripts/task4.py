from pathlib import Path
import openpyxl

BASE_DIR = Path(__file__).resolve().parent.parent
EXCEL_PATH = BASE_DIR / "salary.xlsx"


def read_excel_salaries():
    """Reads salary data from salary.xlsx and prints employee records."""
    if not EXCEL_PATH.exists():
        print(f"File not found: {EXCEL_PATH}")
        return

    wb = openpyxl.load_workbook(EXCEL_PATH)
    sheet = wb.active

    employees = []
    headers = [cell.value for cell in sheet[1]]

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if any(row):
            record = dict(zip(headers, row))
            employees.append(record)

    print(f"Loaded {len(employees)} records from salary.xlsx:")
    for emp in employees:
        print(emp)


if __name__ == "__main__":
    read_excel_salaries()
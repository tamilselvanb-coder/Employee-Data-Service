import csv
from pathlib import Path

# BASE_DIR points to project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Input and output file paths relative to project root
csv_file = BASE_DIR / "employees.csv"
output_file = BASE_DIR / "high_earners.csv"


def process_employees():
    high_earners = []

    # Read input CSV file
    with open(csv_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            salary = float(row["salary"])
            if salary > 60000:
                high_earners.append(row)

    # Write output to high_earners.csv in root directory
    if high_earners:
        fieldnames = high_earners[0].keys()
        with open(output_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(high_earners)

    print(f"Successfully processed {len(high_earners)} high earners to {output_file}")


if __name__ == "__main__":
    process_employees()
import json
from pathlib import Path
import pytest

BASE_DIR = Path(__file__).resolve().parent.parent


def test_api_users_json_exists():
    """Verify api_users.json was generated and is valid JSON."""
    json_path = BASE_DIR / "data" / "api_users.json"
    assert json_path.exists(), "api_users.json file does not exist"

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) > 0


def test_high_earners_csv():
    """Verify high_earners.csv exists and has headers without spaces."""
    csv_path = BASE_DIR / "high_earners.csv"
    assert csv_path.exists(), "high_earners.csv file does not exist"

    with open(csv_path, encoding="utf-8") as f:
        header = f.readline().strip()

    assert header == "name,department,salary"
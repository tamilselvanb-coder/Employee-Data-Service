from pathlib import Path

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setup paths using pathlib
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


def fetch_and_save_data():
    """Fetches sample JSON data from an external API and saves it locally."""
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Output file path
        output_file = DATA_DIR / "api_users.json"

        # Save to JSON file
        import json

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(
            f"Successfully fetched {len(data)} user records and saved to '{output_file.name}'."
        )

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data from API: {e}")


if __name__ == "__main__":
    fetch_and_save_data()

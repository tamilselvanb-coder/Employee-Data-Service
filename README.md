
# Employee Data Service - Week 1 Assessment

A Python-based Employee Data Service built as part of the Yoho Week 1 Assessment. This project demonstrates core Python programming, object-oriented design, file processing (CSV, JSON, Excel, PDF), REST API consumption, HMAC webhook security, FastAPI backend endpoints, and automated testing with pytest.

---

## 📁 Project Structure

```text
Employee Data Service/
│
├── config/             # Configuration files
├── docs/               # Project documentation
├── scripts/            # Executable processing scripts (Task 1 to Task 3)
│   ├── task1.py        # Core Python logic & high earner filtering
│   ├── task2.py        # File handling (CSV, JSON, Excel, PDF)
│   └── task3.py        # REST API client & HMAC webhook validation
├── src/                # FastAPI application source code
├── tests/              # Automated unit tests using pytest
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore file
├── employees.csv       # Input CSV employee data
├── employees.json      # Generated JSON employee data
├── high_earners.csv    # Generated CSV for high earners (>50,000)
├── salary.xlsx         # Generated Excel salary file
├── pyproject.toml      # Black, Ruff, and Pytest configuration
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation and setup guide
```

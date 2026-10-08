# Automated PostgreSQL Database Integration Testing with Pytest

This repository demonstrates a clean integration testing pattern using Pytest and the psycopg2 driver to validate relational database connections and structural data consistency inside an isolated Docker container.

## 🛠️ Infrastructure Stack
* Test Engine: Pytest 8.x
* Database Driver: psycopg2-binary
* Database Target: PostgreSQL 15 (Running in Docker)
* Reporting Tool: pytest-html

## 🚀 Key Engineering Patterns
* Live Integration Checks: The suite establishes a real-time TCP connection to localhost:5432 to query live tables inside the container environment.
* Data Assertion Validation: Uses strict Python native assertions (assert len(rows) > 0) to verify database non-emptiness and readiness states.
* Rich Reporting Integration: Automatically exports a complete technical test report matrix into report.html.

## 💻 Local Testing Protocol
To spin up the tests and update your interactive HTML dashboard locally, run the short command:
pytest test_db_integration.py -v -s --html=report.html

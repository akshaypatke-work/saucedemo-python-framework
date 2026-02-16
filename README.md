# SauceDemo End-to-End Automation Framework (Playwright + Pytest)

## Overview

This project is a comprehensive end-to-end UI automation framework developed using Playwright and Pytest to validate the SauceDemo application. It reflects production-grade automation architecture with a strong focus on scalability, maintainability, and CI/CD readiness.

The framework is designed with scalability, maintainability, and CI-readiness in mind. It follows the **Page Object Model (POM)** design pattern and supports structured test execution using markers.

---

## Tech Stack

- Python
- Playwright
- Pytest
- pytest-xdist (parallel execution)
- pytest-html (HTML reporting)
- GitHub Actions (CI/CD)

---

## Project Structure

saucedemo-python-framework/
│
├── pages/ # Page Object classes
├── tests/ # Test suites
│ ├── auth/
│ ├── ecommerce/
│ ├── products/
│ └── advanced/
│
├── reports/ # Generated HTML reports
├── config/ # Configuration files
├── .github/workflows/ # CI pipeline
│
├── conftest.py # Shared fixtures
├── pytest.ini # Pytest configuration
├── requirements.txt # Dependencies
└── README.md


---


## Helpers Layer

The helpers/ directory centralizes reusable components:

- test_data.py → Stores credentials and static test values
- utils.py → Contains reusable utility functions

This avoids hardcoded values inside test files and improves maintainability.

---

## Features

- Page Object Model implementation
- Reusable login fixture
- Smoke & Regression tagging
- API mocking test
- Visual regression test
- HTML report generation
- Rerun support for flaky tests
- Parallel execution support
- Multi-browser support
- GitHub Actions CI integration

---

## Setup Instructions

### clone repository
git clone https://github.com/akshaypatke-work/saucedemo-python-framework.git
cd saucedemo-python-framework


### create virtual environment
python -m venv venv
source venv/bin/activate


### install dependencies
pip install -r requirements.txt
playwright install


---

## Running Tests

## execute all tests
pytest


## execute in verbose mode
pytest -v


## execute smoke tests
pytest -m smoke


## execute regression tests
pytest -m regression


## execute api tests
pytest -m api


## execute visual tests
pytest -m visual


## Performance Testing (Lighthouse)
This framework includes Lighthouse integration for frontend performance auditing.


## Run Lighthouse Audit
lighthouse https://www.saucedemo.com \
  --output html \
  --output-path reports/lighthouse-report.html \
  --chrome-flags="--headless"


## Open Lighthouse Report
open reports/lighthouse-report.html

## Lighthouse evaluates:
- Performance
- Accessibility
- Best Practices
- SEO


## execute specific test file
pytest tests/auth/test_login.py


## execute specific test function
pytest tests/auth/test_login.py::test_successful_login


## execute in headed mode
pytest --headed


## execute in headed mode with slow motion
pytest --headed --slowmo 500


## execute in parallel
pytest -n auto


## execute in parallel with 4 workers
pytest -n 4


## execute with reruns enabled
pytest --reruns 1


## execute without reruns (stability check)
pytest --reruns 0


## generate html report manually
pytest --html=reports/test-report.html --self-contained-html


## execute and stop on first failure
pytest -x


## Reports
HTML report is generated after test execution.


## generate html report
pytest --html=reports/test-report.html --self-contained-html


## open report (Mac)
open reports/test-report.html


## run tests and open report automatically
pytest --html=reports/test-report.html --self-contained-html && open reports/test-report.html


## Report location:
reports/test-report.html


---

## CI/CD

GitHub Actions pipeline automatically:

- Runs on push to `main`
- Runs on pull requests
- Executes full test suite
- Validates framework stability

---

## Design Decisions

- Implemented Page Object Model for maintainability
- Centralized reusable fixtures in `conftest.py`
- Separated smoke and regression using markers
- Added API mocking for backend simulation
- Integrated CI for automated execution
- Enabled parallel test execution for scalability

---

## Future Improvements

- Environment-based configuration (dev/stage/prod)
- Docker containerization
- Allure reporting integration
- Advanced logging and trace capture
- Test data factory implementation

---

## Documentation

Detailed framework documentation is available here:

[Download Framework Documentation](docs/SauceDemo_Automation_Framework_Documentation.pdf)


## Author

Akshay Patke  
Software Test Engineer
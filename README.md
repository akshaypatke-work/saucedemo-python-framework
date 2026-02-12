# Saucedemo Python Playwright Framework

Automation framework built using:

- Python
- Pytest
- Playwright
- Page Object Model
- Parallel execution (xdist)
- HTML reporting
- API mocking
- Visual regression testing

## Setup

1. Create virtual environment:
   python -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Install Playwright browsers:
   python -m playwright install

## Run Tests

Run all tests:
pytest

Run in parallel:
pytest -n 4

Run with HTML report:
pytest --html=reports/report.html

## Framework Structure

pages/         → Page Object classes  
tests/         → Test cases  
fixtures/      → Pytest fixtures  
helpers/       → Utilities  
config/        → Config files  
reports/       → Reports & screenshots  


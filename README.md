# QA Automation Framework

## 📌 Project Overview

This project is a basic QA automation framework built with:

- Selenium (UI automation)
- Pytest (test runner)
- Requests (API testing)
- Page Object Model (design pattern)
- Allure (test reporting)

The framework demonstrates UI and API automation with reusable fixtures and maintainable test structure.

---

## 🛠 Tech Stack

- Python 3.11
- Selenium
- Pytest
- Requests
- Allure
- GitHub Actions (CI)

---

## 📂 Project Structure

qa-automation-framework/
│
├── tests/               # Test cases
├── pages/               # Page Object classes
├── utils/               # Config and helper files
├── conftest.py          # Pytest fixtures
├── requirements.txt
└── README.md

---

## 🧩 Key Features

- Page Object Model for better maintainability
- Pytest fixtures with setup & teardown
- Parametrize for data-driven testing
- Boundary & negative test cases
- API testing with requests
- Allure test report integration
- CI pipeline using GitHub Actions

---

## 🚀 How to Run Tests

Install dependencies:

pip install -r requirements.txt

Run UI tests:

pytest tests/test_login.py

Run API tests:

pytest tests/test_api.py

Run with Allure report:

pytest --alluredir=reports
allure serve reports

---

## 🎯 Design Decisions

- Used Page Object Model to separate UI locators and test logic.
- Used pytest fixtures to manage browser setup and teardown.
- Used parametrize to improve test coverage.
- Integrated CI to automatically run tests on code push.

---

## 📈 Future Improvements

- Add parallel execution
- Add Docker support
- Integrate test coverage report

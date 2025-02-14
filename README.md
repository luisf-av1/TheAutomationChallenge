# The Automation Challenge

## 📌 Project Overview

This project automates data entry in the **Automation Challenge** form using **Playwright** and **Python**. The test dynamically reads 50 rows from an Excel file (`challenge.xlsx`) and fills in the corresponding form fields while handling CAPTCHA challenges(https://www.theautomationchallenge.com/).

## 📁 Project Structure

```plaintext
TheAutomationChallenge/
│── tests/
│   ├── challenge.py        # Main test execution file
│── pages/
│   ├── login_page.py       # Login page interactions
│   ├── form_page.py        # Form page interactions
│── utils/
│   ├── selectors.py        # Centralized selectors
│   ├── data_reader.py      # Reads challenge.xlsx and maps form fields
│   ├── setup.py            # browser and page setup
│── data/
│   ├── challenge.xlsx      # Excel file with 50 rows of test data
│── requirements.txt        # Required dependencies
│── README.md               # Project documentation
```

---

## 🔧 Setup & Installation

### 1️⃣ **Install Dependencies**

Make sure you have **Python 3.7+** installed. Then, run:

```sh
pip install -r requirements.txt
```

### 2️⃣ **Install Playwright Browsers**

```sh
playwright install
```

or

```sh
python -m playwright install
```

### 3️⃣ **Ensure challenge.xlsx Exists**

Make sure `challenge.xlsx` is inside the `data/` folder. If missing, place the correct Excel file there.

---

## 📄 Required Dependencies (requirements.txt)

To ensure proper execution, the project requires the following dependencies:

- `pytest` → Test framework for running test cases.
- `pytest-playwright` → Integrates Playwright with Pytest for browser automation.
- `playwright` → Main library for browser automation.
- `pandas` → Used for reading and managing `challenge.xlsx` data.
- `openpyxl` → Handles Excel (`.xlsx`) files for test data.

---

## ▶️ Running the Test

To execute the test, run:

```sh
pytest tests/challenge.py
```

or:

```sh
python -m pytest tests/challenge.py
```

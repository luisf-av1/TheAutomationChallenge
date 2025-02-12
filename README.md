# 🚀 Automation Challenge - Playwright & Python

## 📌 Project Overview

This project automates data entry in the **Automation Challenge** form using **Playwright** and **Python**. The test dynamically reads 50 rows from an Excel file (`challenge.xlsx`) and fills in the corresponding form fields while handling CAPTCHA challenges.

## 📁 Project Structure

```plaintext
neostella_python/
│── tests/
│   ├── challenge.py        # Main test execution file
│── pages/
│   ├── login_page.py       # Login page interactions
│   ├── form_page.py        # Form page interactions
│── utils/
│   ├── selectors.py        # Centralized selectors
│   ├── data_reader.py      # Reads challenge.xlsx and maps form fields
│── data/
│   ├── challenge.xlsx      # Excel file with 50 rows of test data
│── requirements.txt        # 📌 Required dependencies
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

### 3️⃣ **Ensure challenge.xlsx Exists**

Make sure `challenge.xlsx` is inside the `data/` folder. If missing, place the correct Excel file there.

---

## 📌 Required Dependencies (requirements.txt)

To ensure proper execution, the project requires the following dependencies:

```plaintext
pytest
pytest-playwright
playwright
pandas
openpyxl
```

**Dependency Breakdown:**

- `pytest` → Test framework for running test cases.
- `pytest-playwright` → Integrates Playwright with Pytest for browser automation.
- `playwright` → Main library for browser automation.
- `pandas` → Used for reading and managing `challenge.xlsx` data.
- `openpyxl` → Handles Excel (`.xlsx`) files for test data.

To install all dependencies, simply run:

```sh
pip install -r requirements.txt
```

---

## 🚀 Running the Test

To execute the test, run:

```sh
pytest tests/challenge.py
```

To run the test with the browser visible (**headed mode**):

```sh
pytest tests/challenge.py --headed
```

---

## 📌 How It Works

### 1️⃣ **Data Extraction from Excel**

The `data_reader.py` script reads `challenge.xlsx` and maps the column names to the form fields:

```python
COLUMN_MAPPING = {
    "company_name": "Company Name",
    "company_address": "Address",
    "employer_identification_number": "EIN",
    "sector": "Sector",
    "automation_tool": "Automation Tool",
    "annual_automation_saving": "Annual Saving",
    "date_of_first_project": "Date"
}
```

This ensures each column in the Excel file matches the correct input field in the form.

### 2️⃣ **Page Object Model (POM)**

We use a **Page Object Model (POM)** approach for better code structure.

#### `login_page.py` (Handles user login)

```python
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
    
    def open(self):
        self.page.goto("https://www.theautomationchallenge.com/", timeout=180000)
    
    def login(self, email="testing@mail.com", password="Test.345"):
        self.page.click(Selectors.BUTTON_GREEN)
        self.page.click(Selectors.BUTTON_BLUE)
        self.page.fill(Selectors.INPUT_EMAIL, email)
        self.page.fill(Selectors.INPUT_PASSWORD, password)
        self.page.click(Selectors.BUTTON_SUBMIT)
        self.page.click(Selectors.BUTTON_GREEN)
```

#### `form_page.py` (Handles form interaction & CAPTCHA solving)

```python
class FormPage:
    def __init__(self, page: Page):
        self.page = page
    
    def handle_captcha(self):
        captcha_popup = self.page.locator(Selectors.CAPTCHA_POPUP)
        if captcha_popup.is_visible():
            captcha_button = captcha_popup.locator(Selectors.CAPTCHA_BUTTON)
            if captcha_button.is_visible():
                captcha_button.wait_for(state='visible', timeout=5000)
                captcha_button.click()
                captcha_popup.wait_for(state='hidden', timeout=5000)
```

### 3️⃣ **Test Execution (****test\_form.py****)**

The test runs 50 times, using a different row from `challenge.xlsx` for each iteration:

```python
for row_data in data_list:
    page.wait_for_timeout(3000)
    form_page.handle_captcha()
    form_page.process_form(row_data)
```

---

## 📌 Key Features

✅ **Reads data dynamically from Excel (****`challenge.xlsx`****)**\
✅ **Handles CAPTCHA pop-ups automatically**\
✅ **Implements Page Object Model (POM) for better structure**\
✅ **Ensures each test iteration uses a new row of data**\
✅ **Runs seamlessly using Playwright + Pytest**

---

## 🛠 Troubleshooting

### **1️⃣ ****`__pycache__/`**** Keeps Appearing**

Python automatically creates `__pycache__/` for performance. To disable it, run:

```sh
PYTHONDONTWRITEBYTECODE=1 pytest tests/challenge.py
```

### **2️⃣ ****`challenge.xlsx`**** Not Found**

Make sure `challenge.xlsx` exists inside the `data/` folder.

### **3️⃣ CAPTCHA Still Blocking the Test**

Try increasing the wait time in `handle_captcha()`:

```python
captcha_button.wait_for(state='visible', timeout=8000)
```

---

## 🎯 Next Steps

- Add more test scenarios.
- Improve CAPTCHA handling.
- Integrate reporting tools like **Allure** for test results.

---

## 🤖 Author

- **Project Developed by:** Andrés Felipe Barrera Mazo
- **Powered by:** Python, Playwright, Pytest

---

🔹 **Hope this README helps! Run the tests and let me know if you need improvements! 🚀🔥**


import sys
import os

# Ensure that `pages/` and `utils/` are in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.form_page import FormPage
from utils.data_reader import read_challenge_data  # 📌 Import the function to read the data

def test_validate_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        form_page = FormPage(page)

        # Open the page and perform login
        login_page.open()
        login_page.login()

        # 📌 Retrieve the first 50 rows from challenge.xlsx
        data_list = read_challenge_data()

        # 🔄 Repeat the process 50 times using data from challenge.xlsx
        for row_data in data_list:
            page.wait_for_timeout(3000)  # Wait before each iteration
            form_page.handle_captcha()
            form_page.process_form(row_data)  # Pass the row as a dictionary

        browser.close()

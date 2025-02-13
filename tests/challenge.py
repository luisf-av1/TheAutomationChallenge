import sys
import os

# Ensure that `pages/` and `utils/` are in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.form_page import FormPage
from utils.data_reader import read_challenge_data
from utils.setup import setUpPage

def test_validate_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # Launch test in backgroung

        page = setUpPage(p)
        page.goto("https://www.theautomationchallenge.com/", wait_until="domcontentloaded")

        # Get required pages (sections)
        login_page = LoginPage(page)
        form_page = FormPage(page)

        
        data_list = read_challenge_data() # Retrieve the first 50 rows from challenge.xlsx
        login_page.login() # LogIn
        login_page.start() # Start challenge

        # Repeat the process 50 times using data from challenge.xlsx
        for row_data in data_list:
            form_page.process_FormPage(row_data)  # Pass the row as a dictionary

        page.wait_for_timeout(2000)
        browser.close()

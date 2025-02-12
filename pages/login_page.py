from playwright.sync_api import Page
from utils.selectors import Selectors  # 📌 Importing the selectors

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

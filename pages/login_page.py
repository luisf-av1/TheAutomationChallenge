import os

from dotenv import load_dotenv
from playwright.sync_api import Page
from utils.selectors import Selectors  # 📌 Importing the selectors


class LoginPage:
    def __init__(self, page: Page):
        load_dotenv() # look for .env file
        self.page = page

    def login(self):        
        self.page.click(Selectors.BUTTON_GREEN)
        self.page.click(Selectors.BUTTON_BLUE)

        #Enter logIng credentials
        self.page.fill(Selectors.INPUT_EMAIL, os.getenv('EMAIL'))
        self.page.fill(Selectors.INPUT_PASSWORD, os.getenv('PASS'))
        self.page.click(Selectors.BUTTON_SUBMIT)

    def start(self):
        self.page.click(Selectors.BUTTON_GREEN) #Start challenge
from playwright.sync_api import Page
from utils.selectors import Selectors  #Importing the selectors from the selectors module

class FormPage:
    def __init__(self, page: Page): 
        # Initializes the FormPage class with a Playwright Page instance.
        self.page = page
        self.captcha_popup = page.locator(Selectors.CAPTCHA_POPUP)
        self.captcha_button = self.captcha_popup.locator(Selectors.CAPTCHA_BUTTON)

    def handle_captcha(self):
        # Method to detects and solves the CAPTCHA challenge if it appears.
        if self.captcha_popup.is_visible():
            print("🔒 CAPTCHA detected, solving...")
            self.captcha_button.click()  # Click on the CAPTCHA button
            self.captcha_popup.wait_for(state='hidden', timeout=3000)
            print("✅ CAPTCHA solved.")

    def process_FormPage(self, data):
        """
        Method to fill out the form fields with given data.
        :param data: Dictionary containing FormPage field labels as keys and corresponding values.
        """
        # Locate all possible FormPage sections that are positioned absolutely
        sections = self.page.locator(Selectors.FORM_SECTION).element_handles() 
        # Filter only the visible FormPage sections
        visible_sections = [section for section in sections if "none" not in section.evaluate("node => node.style.display")]

        if visible_sections:
            current_Form = visible_sections[0]  # Select the new form generated
            inputs = current_Form.query_selector_all("input")  # Get all input fields inside the FormPage

            for input_field in inputs:
                self.handle_captcha()
                label = input_field.evaluate_handle("node => node.closest('.bubble-element.Group')").query_selector(".content") # Try to find the label related to the input
                try:
                    label_text = label.text_content().strip()  # Extract the label text
                    value = data.get(label_text, "")  # Retrieve the corresponding value from the data dictionary
                    input_field.fill(str(value), timeout=2000)  # Faster execution with timeout
                except Exception as e:
                        print(f"⚠️ Could not fill input: {e}")
    
            try:
                submit_button = current_Form.query_selector(Selectors.BUTTON_SUBMIT_FORM)
                submit_button.click(timeout=2000, force=True)
            except:
                print("❌ Submit button not found or not clickable.")

from playwright.sync_api import Page
from utils.selectors import Selectors  # 📌 Importing the selectors from the selectors module

class FormPage:
    def __init__(self, page: Page):
        """
        Initializes the FormPage class with a Playwright Page instance.

        :param page: The Playwright Page instance used for automation.
        """
        self.page = page

    def handle_captcha(self):
        """
        Detects and solves the CAPTCHA challenge if it appears.
        """
        captcha_popup = self.page.locator(Selectors.CAPTCHA_POPUP)  # Locate the CAPTCHA popup
        
        if captcha_popup.is_visible():  # Check if CAPTCHA is visible
            print("🔒 CAPTCHA detected, solving...")

            # Locate the CAPTCHA button inside the popup
            captcha_button = captcha_popup.locator(Selectors.CAPTCHA_BUTTON)

            if captcha_button.is_visible():  # Check if the CAPTCHA button is visible
                captcha_button.wait_for(state='visible', timeout=5000)  # Wait for the button to be clickable
                captcha_button.click()  # Click on the CAPTCHA button
                captcha_popup.wait_for(state='hidden', timeout=5000)  # Wait for the CAPTCHA popup to disappear
                print("✅ CAPTCHA solved.")

    def process_form(self, data):
        """
        Fills in the form fields with data from a given row.

        :param data: Dictionary containing form field labels as keys and corresponding values.
        """
        # Locate all possible form sections that are positioned absolutely
        sections = self.page.locator(Selectors.FORM_SECTION).element_handles()

        # Filter only the visible form sections
        visible_sections = [section for section in sections if "none" not in section.evaluate("node => node.style.display")]

        if visible_sections:
            current_form = visible_sections[0]  # Select the first visible form section
            inputs = current_form.query_selector_all("input")  # Get all input fields inside the form

            for input_field in inputs:
                if input_field.is_visible() and input_field.is_enabled():  # Ensure the input is visible and enabled
                    # Find the closest container for the input (usually a label container)
                    label = input_field.evaluate_handle("node => node.closest('.bubble-element.Group')").query_selector(".content")

                    if label:
                        label_text = label.text_content().strip()  # Extract the label text

                        # 📌 Now using names that match the form fields
                        value = data.get(label_text, "")  # Retrieve the corresponding value from the data dictionary
                        input_field.fill(str(value))  # Fill in the input field with the retrieved value

            # Locate the submit button inside the form
            submit_button = current_form.query_selector(Selectors.BUTTON_SUBMIT_FORM)

            if submit_button:
                submit_button.wait_for_element_state("visible", timeout=5000)  # Wait for the submit button to be visible
                submit_button.click()  # Click the submit button
                self.page.wait_for_load_state("networkidle")  # Wait for the page to finish loading

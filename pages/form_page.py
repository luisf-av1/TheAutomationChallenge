from playwright.sync_api import Page
from utils.selectors import Selectors

class FormPage:
    def __init__(self, page: Page):
        self.page = page

    def handle_captcha(self):
        captcha_popup = self.page.locator(Selectors.CAPTCHA_POPUP)
        if captcha_popup.is_visible():
            print("🔒 CAPTCHA detected, solving...")
            captcha_button = captcha_popup.locator(Selectors.CAPTCHA_BUTTON)
            if captcha_button.is_visible():
                captcha_button.wait_for(state='visible', timeout=5000)
                captcha_button.click()
                captcha_popup.wait_for(state='hidden', timeout=5000)
                print("✅ CAPTCHA solved.")

    def process_form(self, data):
        """Fills in the form fields with data from the row."""
        sections = self.page.locator(Selectors.FORM_SECTION).element_handles()
        visible_sections = [section for section in sections if "none" not in section.evaluate("node => node.style.display")]

        if visible_sections:
            current_form = visible_sections[0]
            inputs = current_form.query_selector_all("input")

            for input_field in inputs:
                if input_field.is_visible() and input_field.is_enabled():
                    label = input_field.evaluate_handle("node => node.closest('.bubble-element.Group')").query_selector(".content")
                    if label:
                        label_text = label.text_content().strip()

                        # 📌 Now using names that match the form
                        value = data.get(label_text, "")  # Look for the value in the data dictionary
                        input_field.fill(str(value))  # Convert to string for safety

            submit_button = current_form.query_selector(Selectors.BUTTON_SUBMIT_FORM)
            if submit_button:
                submit_button.wait_for_element_state("visible", timeout=5000)
                submit_button.click()
                self.page.wait_for_load_state("networkidle")

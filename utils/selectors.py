# utils/selectors.py

class Selectors:
    # Login Page
    BUTTON_GREEN = 'button[class*="bubble-element"][style*="background: none rgb(14, 138, 5)"]'
    BUTTON_BLUE = 'button[class*="bubble-element"][style*="rgb(58, 77, 143)"]'
    INPUT_EMAIL = 'input[placeholder="Email"]'
    INPUT_PASSWORD = 'input[type="password"]'
    BUTTON_SUBMIT = 'button[class*="bubble-element"][style*="rgb(255, 255, 255); border: 2px solid rgb(0, 0, 0);"]'

    # CAPTCHA
    CAPTCHA_POPUP = 'div.bubble-element.Popup[style*="background-color: rgb(255, 255, 255)"]'
    CAPTCHA_BUTTON = 'button.bubble-element.Button.clickable-element[style*="background: none rgb(255, 255, 255)"]'

    # Form Page
    FORM_SECTION = '.main-page > :last-child > div > .Group[style*="position: absolute;"]'
    BUTTON_SUBMIT_FORM = 'button.bubble-element.Button.clickable-element'

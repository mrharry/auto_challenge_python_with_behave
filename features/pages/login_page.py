from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class LoginPage(BasePage):
    locator_dictionary = {
        "login_email": (By.ID, "login_email"),
        "login_password": (By.ID, "login_password"),
        "login_button": (By.CLASS_NAME, "session_submit_button"),
        "login_creds_error_message": (By.CSS_SELECTOR, "div.flash")
    }

    def __init__(self, browser):
        super().__init__(browser)

    def fill_login_credentials(self, cred_type, context):
        if cred_type == "invalid":
            self.submit(*self.locator_dictionary['login_button'])
        else:
            self.fill_in(context.config.userdata.get('email'), *self.locator_dictionary['login_email'])
            self.fill_in(context.config.userdata.get('password'), *self.locator_dictionary['login_password'])
            self.submit(*self.locator_dictionary['login_button'])

    def creds_error_message(self):
        return self.text_of(*self.locator_dictionary['login_creds_error_message'])

from playwright.sync_api import Page

from .selectors import Selectors


class TestLoginPOM:

    def __init__(self, page: Page):
        self.page = page
        self.selectors = Selectors

    def navigate_to_login_page(self, url):
        self.page.goto(url)

    def type_in_username(self, username):
        self.page.locator(self.selectors.USERNAME_INPUT).fill(username)

    def type_in_password(self, password):
        self.page.locator(self.selectors.PASSWORD_INPUT).fill(password)

    def push_submit_button(self):
        self.page.locator(self.selectors.SUBMIT_BUTTON).click()

    def get_congratulation_message(self):
        return self.page.locator(self.selectors.CONGRATULATION_MESSAGE)

    def get_log_out_button_element(self):
        return self.page.locator(self.selectors.LOG_OUT_BUTTON)

    def get_error_message_element(self):
        return self.page.locator(self.selectors.ERROR_MESSAGE)


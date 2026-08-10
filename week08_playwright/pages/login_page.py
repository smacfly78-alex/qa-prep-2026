from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://the-internet.herokuapp.com/login'

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.get_by_label('Username')
        self.password_input = page.get_by_label('Password')
        self.login_button = page.get_by_role('button', name = 'Login')

    def open(self) -> "LoginPage":
        self.page.goto(self.URL)
        return self

    def enter_username(self, username) -> "LoginPage":
        self.username_input.fill(username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        self.password_input.fill(password)
        return self

    def click_login(self) -> "SecurePage":
        from pages.secure_page import SecurePage
        self.login_button.click()
        return SecurePage(self.page)

    def login(self, username: str, password: str) -> "SecurePage":
        from pages.secure_page import SecurePage
        self.enter_username(username).enter_password(password).click_login()
        return SecurePage(self.page)


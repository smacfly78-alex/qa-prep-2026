from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from week07_selenium.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    URL = "https://the-internet.herokuapp.com/login"

    def open(self) -> "LoginPage":
        self.driver.get(self.URL)
        return self

    def enter_username(self, username: str) -> "LoginPage":
        self.wait.until(EC.visibility_of_element_located(LoginPage.USERNAME_INPUT)).send_keys(username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        self.wait.until(EC.visibility_of_element_located(LoginPage.PASSWORD_INPUT)).send_keys(password)
        return self

    def click_login(self):
        from week07_selenium.pages.secure_page import SecurePage
        self.wait.until(EC.element_to_be_clickable(LoginPage.LOGIN_BUTTON)).click()
        return SecurePage(self.driver)

    def login(self, username: str, password:str):
        from week07_selenium.pages.secure_page import SecurePage
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return SecurePage(self.driver)
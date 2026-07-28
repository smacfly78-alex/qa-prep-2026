from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: webdriver.Chrome) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_title(self) -> str:
        return self.driver.title
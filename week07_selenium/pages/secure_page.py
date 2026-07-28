from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from week07_selenium.pages.base_page import BasePage


class SecurePage(BasePage):
    FLASH_MESSAGE = (By.ID, "flash")

    def get_message(self) -> str:
        text_message = self.wait.until(EC.visibility_of_element_located(SecurePage.FLASH_MESSAGE)).text
        return text_message

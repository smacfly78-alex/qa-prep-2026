from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from week07_selenium.pages.login_page import LoginPage


def run() -> None:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        secure_page = LoginPage(driver).open().login("tomsmith", "SuperSecretPassword!")
        print(f"Message: {secure_page.get_message()}")
        print(f"URL: {secure_page.get_current_url()}")
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
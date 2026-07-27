from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def cookies_and_js_demo(driver: webdriver.Chrome) -> None:
    # Часть 1: логин + чтение cookies
    driver.get('https://the-internet.herokuapp.com/login')
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, 'username'))).send_keys('tomsmith')
    wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys('SuperSecretPassword!')
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.radius'))).click()

    wait.until(EC.visibility_of_element_located((By.ID, 'flash')))

    cookies = driver.get_cookies()
    for cookie in cookies:
        print(cookie['name'])

    cookie_rack = driver.get_cookie('rack.session')
    print(cookie_rack)

    print(driver.execute_script('return document.title;'))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print(driver.execute_script("return window.location.href;"))


def run() -> None:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        cookies_and_js_demo(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
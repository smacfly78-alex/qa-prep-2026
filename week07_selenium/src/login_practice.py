from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login_demo(driver: webdriver.Chrome, username: str, password: str) -> None:
    driver.get('https://the-internet.herokuapp.com/login')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'username'))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(password)
    button_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.radius')))
    button_login.click()

    text_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'flash'))).text
    print(text_field)
    print(driver.current_url)



def run() -> None:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        login_demo(driver, 'tomsmith', 'SuperSecretPassword!')
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
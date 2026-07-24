from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def dynamic_loading_demo(driver) -> None:
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    wait = WebDriverWait(driver, 10)

    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#start button')))
    button.click()

    result = wait.until(EC.visibility_of_element_located((By.ID, 'finish')))
    print(result)



def run() -> None:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        dynamic_loading_demo(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def iframe_demo(driver: webdriver.Chrome) -> None:
    driver.get('https://the-internet.herokuapp.com/iframe')
    wait = WebDriverWait(driver, 10)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

    el = wait.until(EC.visibility_of_element_located((By.ID, 'tinymce')))
    print(el.text)
    el.send_keys(Keys.CONTROL, 'a')
    el.send_keys(Keys.BACKSPACE)
    el.send_keys('Hello from Selenium!')

    driver.switch_to.default_content()


def alerts_demo(driver: webdriver.Chrome) -> None:
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text() = "Click for JS Confirm"]'))).click()
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    alert.dismiss()
    result = wait.until(EC.visibility_of_element_located((By.ID, 'result'))).text
    print(result)



def run() -> None:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        iframe_demo(driver)
        alerts_demo(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
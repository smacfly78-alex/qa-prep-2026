from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def explore_login_page(driver: webdriver.Chrome) -> None:
    driver.get('https://the-internet.herokuapp.com/login')

    heading = driver.find_element(By.TAG_NAME, "h2")
    print(f"Heading: {heading.text}")

    username_by_id = driver.find_element(By.ID, "username")
    print(f"By ID: tag={username_by_id.tag_name}, name={username_by_id.get_attribute('name')}")

    username_by_name = driver.find_element(By.NAME, "username")
    print(f"By NAME: tag={username_by_name.tag_name}, id={username_by_name.get_attribute('id')}")

    username_by_css = driver.find_element(By.CSS_SELECTOR, "#username")
    print(f"By CSS: tag={username_by_css.tag_name}")

    login_by_css = driver.find_element(By.CSS_SELECTOR, "button.radius")
    print(f"Login by CSS: tag={login_by_css.tag_name}")

    login_by_xpath = driver.find_element(By.XPATH, "//button[@type='submit']")
    print(f"Login by XPATH: tag={login_by_xpath.tag_name}")

    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"Total inputs: {len(inputs)}")


def run() -> None:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        explore_login_page(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    run()


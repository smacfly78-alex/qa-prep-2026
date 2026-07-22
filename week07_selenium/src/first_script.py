from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def explore(driver) -> None:
    driver.get("https://www.example.com")
    print(driver.title)
    driver.get("https://www.python.org")
    print(driver.title)
    driver.back()
    driver.forward()
    print(driver.title)
    print(driver.current_url)
    driver.back()
    print(driver.current_url)
    driver.refresh()

def run() -> None:
    """Opens Google, prints title, closes browser."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        explore(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
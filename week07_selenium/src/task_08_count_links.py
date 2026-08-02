from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def count_links(driver: webdriver.Chrome, url: str) -> None:
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    links_a = driver.find_elements(By.TAG_NAME, 'a')
    print(len(links_a))

    for link_a in links_a[:5]:
        print(link_a.get_attribute('href'))

def run() -> None:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        count_links(driver, "https://the-internet.herokuapp.com/")
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

def page_info(page: Page, url: str) -> None:
    page.goto(url)

    print(page.title())
    print(page.url)
    page.screenshot(path="screenshot.png")
    print(page.viewport_size)


def run() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page_info(page, "https://the-internet.herokuapp.com/")

        browser.close()


if __name__ == "__main__":
    run()
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def get_url(self) -> str:
        return self.page.url

    def get_title(self) -> str:
        return self.page.title()
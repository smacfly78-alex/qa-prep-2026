from playwright.sync_api import sync_playwright, Page


def find_login_button(page: Page) -> None:
    print(page.get_by_role('button', name='Login').is_visible())
    print(page.get_by_text("Login", exact=True).count())
    print(page.locator("button[type='submit']").is_visible())
    print(page.locator('//button[text()= "Login"]').is_visible())
    print(page.locator("#login button").is_visible())
    print(page.get_by_role("button").filter(has_text="Login").is_visible())
    print(page.locator("//button[@type='submit']").is_visible())

def login_via_semantic(page, username, password):
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    print(page.get_by_text("You logged").text_content())


def run() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")

        # Часть 1 — найти кнопку 6 способами
        find_login_button(page)

        # Часть 2 — логин через семантические
        login_via_semantic(page, "tomsmith", "SuperSecretPassword!")

        browser.close()

if __name__ == '__main__':
    run()
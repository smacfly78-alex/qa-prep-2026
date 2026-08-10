from playwright.sync_api import expect
from pages.login_page import LoginPage
import re


def test_valid_login(page):
    secure_page = LoginPage(page).open().login("tomsmith", "SuperSecretPassword!")

    expect(page).to_have_url(re.compile(r".*/secure"))
    expect(secure_page.flash_message).to_contain_text("You logged into")
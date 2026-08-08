from playwright.sync_api import sync_playwright, expect


def checkbox_demo(page):
    page.goto('https://the-internet.herokuapp.com/checkboxes')

    page.get_by_role('checkbox').first.check()
    page.get_by_role('checkbox').last.check()

    expect(page.get_by_role('checkbox').first).to_be_checked()
    expect(page.get_by_role('checkbox').last).to_be_checked()

    page.get_by_role('checkbox').first.uncheck()
    expect(page.get_by_role('checkbox').first).not_to_be_checked()
    expect(page.get_by_role('checkbox').last).to_be_checked()

def dropdown_demo(page):
    page.goto('https://the-internet.herokuapp.com/dropdown')

    page.get_by_role("combobox").select_option(label = 'Option 1')
    expect(page.get_by_role("combobox")).to_have_value('1')

    page.get_by_role("combobox").select_option(value= '1')
    expect(page.get_by_role("combobox")).to_have_value('1')

    page.get_by_role("combobox").select_option(index=1)
    expect(page.get_by_role("combobox")).to_have_value('1')

def login_with_assertions(page):
    page.goto('https://the-internet.herokuapp.com/login')

    page.get_by_role('textbox', name= 'Username').fill('tomsmith')
    page.get_by_role('textbox', name= 'Password').fill('SuperSecretPassword!')

    page.get_by_role('button', name= 'Login').click()
    page.wait_for_url("**/secure")

    import re
    expect(page).to_have_url(re.compile(r".*/secure"))
    expect(page.locator("#flash")).to_contain_text("You logged into")

    print('Login successful')


def run() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Часть 1
        page1 = browser.new_page()
        checkbox_demo(page1)
        page1.close()

        # Часть 2
        page2 = browser.new_page()
        dropdown_demo(page2)
        page2.close()

        # Часть 3
        page3 = browser.new_page()
        login_with_assertions(page3)
        page3.close()

        browser.close()

if __name__ == '__main__':
    run()
from playwright.sync_api import Page, expect


def test_invalid_login(page: Page, login_page):
    page.goto('https://www.saucedemo.com/')
    login_page.user_name.fill('Test')
    login_page.password.fill('Panda')
    login_page.login_button.click()
    expect(login_page.error_msg_container).to_contain_text("Epic sadface: Username and password do not match any user "
                                                           "in this service")


def test_locked_out_user(page: Page, login_page):
    page.goto('https://www.saucedemo.com/')
    login_page.user_name.fill('locked_out_user')
    login_page.password.fill('secret_sauce')
    login_page.login_button.click()
    expect(login_page.error_msg_container).to_contain_text("Epic sadface: Sorry, this user has been locked out.")

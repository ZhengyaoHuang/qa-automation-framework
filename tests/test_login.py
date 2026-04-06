from pages.login_page import LoginPage

def test_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")

    assert page.is_login_successful()
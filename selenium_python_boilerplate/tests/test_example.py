
from selenium_python_boilerplate.pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "https://www.selenium.dev"
    page = MainPage(browser, link)
    page.open()
    page.should_has_selenium_driver_icon()

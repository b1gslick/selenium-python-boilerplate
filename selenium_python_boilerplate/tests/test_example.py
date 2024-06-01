
from selenium_python_boilerplate.pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser, base_url):
    page = MainPage(browser, base_url)
    page.open()
    page.should_has_selenium_driver_icon()

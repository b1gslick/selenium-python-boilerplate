
from selenium_python_boilerplate.pages.main_page import MainPage
from selenium_python_boilerplate.helpers.locators import ExampleLocators

def test_guest_can_go_to_login_page(browser):
    link = "https://www.selenium.dev"
    page = MainPage(browser, link)
    page.open()
    page.should_has_input_field(ExampleLocators.SELENIUM_WEBDRIVER_ICON)

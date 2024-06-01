import pytest
import os
from selenium import webdriver

from selenium_python_boilerplate.helpers.loging import write_log



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None

    write_log(f"start test for browser: {browser_name}")
    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    write_log("Quit browser")
    browser.quit()

@pytest.fixture(scope="function")
def base_url():
    return os.environ.get("BASE_URL", "https://www.selenium.dev")

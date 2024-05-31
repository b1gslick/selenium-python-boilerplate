from typing import Optional, Tuple
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, browser, url: str, timeout: int=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what: str, timeout: Optional[int] = None):
        if not timeout:
            timeout = self.timeout
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what: str, timeout: Optional[int] = None):
        if not timeout:
            timeout = self.timeout
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_has_input_field(self, locator: Tuple[str, str]):
        assert self.is_element_present(*locator)

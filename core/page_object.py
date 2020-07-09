from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import config
import global_objects


class PageObject:

    def __init__(self, xpath):
        self.xpath: str = xpath
        self.selenium_element = None
        self.driver = global_objects.driver
        self.find()

    def __getattr__(self, item):
        return getattr(self.selenium_element, item)


class FindElement(PageObject):

    def find(self):
        wait = WebDriverWait(self.driver, config.FIND_EL_TIMEOUT)
        wait.until(ec.visibility_of_element_located((By.XPATH, self.xpath)))
        self.selenium_element = self.driver.find_element(By.XPATH, self.xpath)


class FindElements(PageObject):

    def find(self):
        self.selenium_element = self.driver.find_elements(By.XPATH, self.xpath)


def find_elm(xpath: str) -> PageObject:
    return FindElement(xpath)


def find_elms(xpath: str) -> PageObject:
    return FindElements(xpath)

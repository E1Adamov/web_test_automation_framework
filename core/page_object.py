from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PageObject:

    def __init__(self, driver, xpath):
        self.xpath: str = xpath
        self.selenium_element = None
        self.driver = driver

    def __getattr__(self, item):
        self.wait()
        return getattr(self.selenium_element, item)


class FindElement(PageObject):

    def wait(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, self.xpath)))
        self.selenium_element = self.driver.find_element(By.XPATH, self.xpath)
        return self.selenium_element


class FindElements(PageObject):

    def wait(self):
        self.selenium_element = self.driver.find_elements(By.XPATH, self.xpath)
        return self.selenium_element


def find_el(driver, xpath: str) -> PageObject:
    return FindElement(driver, xpath)


def find_els(driver, xpath: str) -> PageObject:
    return FindElements(driver, xpath)

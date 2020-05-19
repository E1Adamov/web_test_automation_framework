class PageObject:
    """
    wait for self.selenium_element (visible)
    redirect all calls to self.selenium_element
    """
    def __init__(self, xpath):
        self.xpath: str = xpath
        self.selenium_element = None


def find(xpath: str) -> PageObject:
    return PageObject(xpath)
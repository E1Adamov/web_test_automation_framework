from selenium import webdriver


def get_webdriver(webdriver_alias: str):
    webdriver_alias_map = dict(
        chrome=webdriver.Chrome,
        firefox=webdriver.Firefox,
        ie=webdriver.Ie
    )
    webdriver_instance = webdriver_alias_map[webdriver_alias]()
    return webdriver_instance

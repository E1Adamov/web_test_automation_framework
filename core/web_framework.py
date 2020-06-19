from locators import MainPage
from core.page_object import find_el


def web_framework(test_case: callable):
    """
    open https://flask.io/
    click "get started" if needed

    runs test

    make_report()
    """
    def wrapper(*a, **k):
        driver = k['driver']
        driver.get("https://flask.io/")
        find_el(driver, MainPage.create_todo_btn).click()
        test_case(driver)
        driver.quit()
    return wrapper

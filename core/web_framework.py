from locators import MainPage
from core.page_object import find_elm
import global_objects


def web_framework(test_case: callable):
    """
    open https://flask.io/
    click "get started" if needed

    runs test

    make_report()
    """
    def wrapper(*a, **k):
        driver = global_objects.driver
        driver.get("https://flask.io/")
        find_elm(MainPage.create_todo_btn).click()
        test_case()
        driver.quit()
    return wrapper

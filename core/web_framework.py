from selenium.webdriver.common.by import By
from locators import MainPage


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
        driver.find_element(By.CLASS_NAME, MainPage.create_todo_btn).click()
        test_case(driver)
        driver.quit()
    return wrapper

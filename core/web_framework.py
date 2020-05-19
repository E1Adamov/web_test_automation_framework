from selenium import webdriver
from selenium.webdriver.common.by import By


def web_framework(test_case):
    """
    open https://flask.io/
    click "get started" if needed

    runs test

    make_report()
    """
    driver = webdriver.Chrome('C:\\Users\\kpolo\\PycharmProjects\\web_test_fm\\chromedriver.exe')
    driver.get("https://flask.io/")
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    test_case(driver)
    driver.quit()

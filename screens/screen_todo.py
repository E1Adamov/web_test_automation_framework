from core.page_object import find
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from core.todo import Todo
from locators import CreateToDo, ExistingToDO


def create_new_todo(to_do, driver):
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.ID, CreateToDo.enter_task)))
    task = driver.find_element(By.ID, CreateToDo.enter_task)
    task.send_keys(to_do.text)
    task.send_keys(Keys.ENTER)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, CreateToDo.enter_date)))
    driver.find_element(By.CLASS_NAME, CreateToDo.enter_date).click()
    driver.find_element(By.XPATH, CreateToDo.enter_month).click()
    driver.find_element(By.XPATH, CreateToDo.choose_month + to_do.due_date.strftime("%b") + "')]").click()
    driver.find_element(By.XPATH, CreateToDo.enter_year).click()
    driver.find_element(By.XPATH, CreateToDo.choose_year + to_do.due_date.strftime("%Y") + "')]").click()
    driver.find_element(By.XPATH, CreateToDo.choose_day + to_do.due_date.strftime("%#d") +
                        "')]").click()


def get_existing_todos(driver):
    todos_info = []
    list_of_todo = driver.find_elements(By.XPATH, ExistingToDO.list_of_todo)
    list_of_done = driver.find_elements(By.XPATH, ExistingToDO.list_of_done)
    for i in range(1, len(list_of_todo) + 1):
        todo_text = driver.find_element(By.XPATH, "//ul[contains(@class, 'todo ui-sortable')]/li[" + str(i) +
                                        "]/form/span[2]").text
        todo_due_date = driver.find_element(By.XPATH, "//ul[contains(@class, 'todo ui-sortable')]/li[" + str(i) +
                                            "]/form/span[3]").text
        todo_info = Todo(text=todo_text)
        todo_info.new_todo_due_date = todo_due_date
        todos_info.append(todo_info)
    for i in range(1, len(list_of_done) + 1):
        todo_text = driver.find_element(By.XPATH, "//ul[contains(@class, 'done ui-sortable')]/li[" + str(i) +
                                        "]/form/span[2]").text
        todo_due_date = driver.find_element(By.XPATH, "//ul[contains(@class, 'done ui-sortable')]/li[" + str(i) +
                                            "]/form/span[3]").text
        todo_info = Todo(text=todo_text, is_open=False)
        todo_info.new_todo_due_date = todo_due_date
        todos_info.append(todo_info)
    return todos_info

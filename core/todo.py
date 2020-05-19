from datetime import datetime as dt

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class Todo:
    """
    text
    due_date
    status
    """
    def __init__(self, text, due_date, is_open):
        self.text: str = text
        self.due_date: str = ""
        self.is_open: bool = is_open

    @property
    def new_todo_due_date(self):
        return due_date

    @new_todo_due_date.setter
    def new_todo_due_date(self, new_date: str) -> dt:
        """
        validate new_date -> raise TypeError if not is_valid()
        converts str to datetime format
        """
        pass




    # def create_new_todo(self, driver):
    #     wait = WebDriverWait(driver, 10)
    #     wait.until(ec.visibility_of_element_located((By.ID, "list_tasks_attributes_0_description")))
    #     task = driver.find_element(By.ID, "list_tasks_attributes_0_description")
    #     task.send_keys(self.new_todo_text)
    #     task.send_keys(Keys.ENTER)
    #     wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "due_date")))
    #     driver.find_element(By.CLASS_NAME, "due_date").click()
    #     driver.find_element(By.XPATH, "//div[1][contains(@class, 'pika-label')]").click()
    #     driver.find_element(By.XPATH, "//option[contains(text(), '" + self.new_todo_due_date[0] + "')]").click()
    #     driver.find_element(By.XPATH, "//div[2][contains(@class, 'pika-label')]").click()
    #     driver.find_element(By.XPATH, "//option[contains(text(), '" + self.new_todo_due_date[2] + "')]").click()
    #     driver.find_element(By.XPATH, "//button[contains(@data-pika-day, '" + str(int(self.new_todo_due_date[1])) +
    #                         "')]").click()
    #
    # def existing_todos(self, driver):
    #     todos_info = []
    #     list_of_todo = driver.find_elements(By.XPATH, "//ul[contains(@class, 'todo ui-sortable')]/li")
    #     for i in range(1, len(list_of_todo)+1):
    #         todo_info = []
    #         todo_text = driver.find_element(By.XPATH, "//ul[contains(@class, 'todo ui-sortable')]/li[" + str(i) +
    #                                         "]/form/span[2]").text
    #         todo_due_date = driver.find_element(By.XPATH, "//ul[contains(@class, 'todo ui-sortable')]/li[" + str(i) +
    #                                             "]/form/span[3]").text
    #         todo_info.append(todo_text)
    #         todo_info.append(todo_due_date)
    #         todos_info.append(todo_info)
    #     return todos_info
    #
    # def verify(self, todo_info, todo_info_check):
    #     todo_info[1][0] = todo_info[1][0][0:3]
    #     if todo_info[0] in todo_info_check[0] and " ".join(todo_info[1]) in todo_info_check[1]:
    #         print('Successfully created new todo')
    #     else:
    #         print('Sth go wrong')
    #         print(todo_info)
    #         print(todo_info_check)
    #
    #
    #







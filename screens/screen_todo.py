from core.page_object import *
from selenium.webdriver.common.keys import Keys
from core.todo import Todo
from locators import CreateToDo, ExistingToDO


class ScreenToDo:
    def create_new_todo(self, to_do, driver):
        find_el(driver, CreateToDo.enter_task).send_keys(to_do.text + Keys.ENTER)
        if to_do.due_date != "":
            find_el(driver, CreateToDo.enter_date).click()
            find_el(driver, CreateToDo.enter_month).click()
            find_el(driver, CreateToDo.choose_month.format(to_do.due_date.strftime("%b"))).click()
            find_el(driver, CreateToDo.enter_year).click()
            find_el(driver, CreateToDo.choose_year.format(to_do.due_date.strftime("%Y"))).click()
            find_el(driver, CreateToDo.choose_day.format(to_do.due_date.strftime("%#d"))).click()

    def get_existing_todos(self, driver):
        todos_info = []
        list_of_todo = find_els(driver, ExistingToDO.list_of_todo).wait()
        list_of_done = find_els(driver, ExistingToDO.list_of_done).wait()
        for i in range(1, len(list_of_todo) + 1):
            todo_text = find_el(driver, ExistingToDO.todo_text.format(str(i))).text
            todo_due_date = find_el(driver, ExistingToDO.todo_due_date.format(str(i))).text
            todo_info = Todo(text=todo_text, due_date=todo_due_date)
            todos_info.append(todo_info)
        for i in range(1, len(list_of_done) + 1):
            todo_text = find_el(driver, ExistingToDO.todo_text.format(str(i))).text
            todo_due_date = find_el(driver, ExistingToDO.todo_due_date.format(str(i))).text
            todo_info = Todo(text=todo_text, due_date=todo_due_date, is_open=False)
            todos_info.append(todo_info)
        return todos_info

from core.page_object import *
from selenium.webdriver.common.keys import Keys
from core.todo import Todo
from locators import CreateToDo, ExistingToDO


class ScreenToDo:

    def create_new_todo(self, to_do):
        find_elm(CreateToDo.enter_task).send_keys(to_do.text + Keys.ENTER)
        if to_do.due_date != "":
            find_elm(CreateToDo.enter_date).click()
            find_elm(CreateToDo.enter_month).click()
            find_elm(CreateToDo.choose_month.format(to_do.due_date.strftime("%b"))).click()
            find_elm(CreateToDo.enter_year).click()
            find_elm(CreateToDo.choose_year.format(to_do.due_date.strftime("%Y"))).click()
            find_elm(CreateToDo.choose_day.format(to_do.due_date.strftime("%#d"))).click()

    def get_existing_todos(self):
        todos = []
        list_of_todo = find_elms(ExistingToDO.list_of_todo).selenium_element
        list_of_done = find_elms(ExistingToDO.list_of_done).selenium_element
        for i in range(1, len(list_of_todo) + 1):
            todo_text = find_elm(ExistingToDO.todo_text.format(str(i))).text
            todo_due_date = find_elm(ExistingToDO.todo_due_date.format(str(i))).text
            todo = Todo(text=todo_text, due_date=todo_due_date)
            todos.append(todo)
        for i in range(1, len(list_of_done) + 1):
            todo_text = find_elm(ExistingToDO.todo_text.format(str(i))).text
            todo_due_date = find_elm(ExistingToDO.todo_due_date.format(str(i))).text
            todo = Todo(text=todo_text, due_date=todo_due_date, is_open=False)
            todos.append(todo)
        return todos

import argparse
import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath+'/../')

from core.webdriver_factory import WebdriverFactory
from typing import List
from core.todo import Todo
from core.web_framework import web_framework
from screens import screen_factory as screen
from core.verify import verify


@web_framework
def test_create_new_todo(driver):
    '''new_todo: Todo = Todo(text='Hello Blat')
    create_new_todo(text=new_todo_text)
    exisiting_todos: List[Todo] = get_existing_todos()  ?зачем
    new_todo_exists = new_todo in exisiting_todos
    verify(param_1=new_todo_exists, param_2=True, operator='==')  ? не понимаю способа проверки'''
    to_do = Todo(text='Hello Blat', due_date='Wed Jul 05 2023')
    print(to_do.due_date)
    screen("screen1").create_new_todo(to_do, driver)
    existing_todos: List = get_existing_todos(driver)
    assert verify(arg_1=to_do.text in existing_todos[0].text, arg_2=True, operator='==')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', help="Browser name 'chrome', 'ie', 'firefox'")
    args = parser.parse_args()
    driver = args.browser
    driver = WebdriverFactory.get_webdriver(driver)
    test_create_new_todo(driver=driver)



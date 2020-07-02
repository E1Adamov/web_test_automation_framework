import argparse
import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath+'/../')

from webdriver_factory import get_webdriver
from typing import List
from core.todo import Todo
from core.web_framework import web_framework
from screens.screen_factory import screen
from core.verify import verify
import global_objects


@web_framework
def test_create_new_todo():
    to_do = Todo(text='Hello Blat', due_date='Wed Jul 05 2023')
    # to_do = Todo(text='Hello Blat')
    screen('todo').create_new_todo(to_do)
    existing_todos: List = screen("todo").get_existing_todos()
    assert verify(to_do == existing_todos[0], True, operator='==')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', help="Browser name 'chrome', 'ie', 'firefox'")
    args = parser.parse_args()
    driver = args.browser
    global_objects.driver = get_webdriver(driver)
    test_create_new_todo(driver=global_objects.driver)



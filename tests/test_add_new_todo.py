import argparse
import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath+'/../')

from core.webdriver_factory import WebdriverFactory
from typing import List
from core.todo import Todo
from core.web_framework import web_framework
from screens.screen_factory import screen
from core.verify import verify


@web_framework
def test_create_new_todo(driver):
    to_do = Todo(text='Hello Blat', due_date='Wed Jul 05 2023')
    # to_do = Todo(text='Hello Blat')
    screen('todo').create_new_todo(to_do, driver)
    existing_todos: List = screen("todo").get_existing_todos(driver)
    assert verify(arg_1=to_do.text in existing_todos[0].text, arg_2=True, operator='==')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', help="Browser name 'chrome', 'ie', 'firefox'")
    args = parser.parse_args()
    driver = args.browser
    driver = WebdriverFactory.get_webdriver(driver)
    test_create_new_todo(driver=driver)



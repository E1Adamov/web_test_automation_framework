from typing import List
from core.todo import Todo
from core.web_framework import web_framework


@web_framework
def test_create_new_todo(driver):
    '''new_todo: Todo = Todo(text='Hello Blat')
    create_new_todo(text=new_todo_text)
    exisiting_todos: List[Todo] = get_existing_todos()  ?зачем
    new_todo_exists = new_todo in exisiting_todos
    verify(param_1=new_todo_exists, param_2=True, operator='==')  ? не понимаю способа проверки'''
    to_do = Todo('Hello Blat', 'June 05 2021', True)
    create_new_todo(driver)
    existing_todos: List = get_existing_todos(driver)
    assert verify([to_do.new_todo_text, to_do.new_todo_due_date], existing_todos[0])


if __name__ == '__main__':
    args = parse_args()
    driver = args.driver
    test_create_new_todo(driver=driver)



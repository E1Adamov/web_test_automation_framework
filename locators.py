class MainPage:
    create_todo_btn = "//*[contains(@class, 'btn-primary')]"


class CreateToDo:
    enter_task = "//*[@id = 'list_tasks_attributes_0_description']"
    enter_date = "//*[contains(@class, 'due_date')]"
    enter_month = "//div[1][contains(@class, 'pika-label')]"
    enter_year = "//div[2][contains(@class, 'pika-label')]"
    choose_month = "//option[contains(text(), '{}')]"
    choose_year = "//option[contains(text(), '{}')]"
    choose_day = "//button[contains(@data-pika-day, '{}')]"


class ExistingToDO:
    list_of_todo = "//ul[contains(@class, 'todo ui-sortable')]/li"
    list_of_done = "//ul[contains(@class, 'done ui-sortable')]/li"
    todo_text = "//ul[contains(@class, 'todo ui-sortable')]/li[{}]/form/span[2]"
    todo_due_date = "//ul[contains(@class, 'todo ui-sortable')]/li[{}]/form/span[3]"

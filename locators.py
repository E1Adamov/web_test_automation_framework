class MainPage:
    create_todo_btn = "btn-primary"


class CreateToDo:
    enter_task = "list_tasks_attributes_0_description"
    enter_date = "due_date"
    enter_month = "//div[1][contains(@class, 'pika-label')]"
    enter_year = "//div[2][contains(@class, 'pika-label')]"
    choose_month = "//option[contains(text(), '"
    choose_year = "//option[contains(text(), '"
    choose_day = "//button[contains(@data-pika-day, '"


class ExistingToDO:
    list_of_todo = "//ul[contains(@class, 'todo ui-sortable')]/li"
    list_of_done = "//ul[contains(@class, 'done ui-sortable')]/li"

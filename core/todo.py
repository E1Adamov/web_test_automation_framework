from datetime import datetime as dt


class Todo:
    """
    text
    due_date
    status
    """
    def __init__(self, text, due_date="", is_open=True):
        self.text: str = text
        self.due_date: str = due_date
        self.is_open: bool = is_open

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, new_date: str) -> dt:
        """
        validate new_date -> raise TypeError if not is_valid()
        converts str to datetime format
        """
        if new_date != "":
            try:
                self.__due_date = dt.strptime(new_date, '%a %b %d %Y')
            except ValueError as e:
                raise e
        else:
            self.__due_date = ""







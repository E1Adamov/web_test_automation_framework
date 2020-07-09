from typing import Union
from screens.screen_todo import ScreenToDo


def screen(screen_alias: str) -> Union[ScreenToDo]:
    screen_alias_map = dict(
        todo=ScreenToDo
    )
    screen_instance = screen_alias_map[screen_alias]()
    return screen_instance

from typing import Callable
from pydantic import BaseModel

from sclick.enums import PageEnum


class AppState(BaseModel):
    current_page: PageEnum


class AppModel:
    def __init__(self):
        self.state = AppState(current_page=PageEnum.ENTRY)
        self.page_observers: list[Callable[[PageEnum], None]] = []

    def register_page_observer(self, observer: Callable[[PageEnum], None]):
        self.page_observers.append(observer)

    def remove_page_observer(self, observer: Callable[[PageEnum], None]):
        # TODO: not sure if this will work, test it.
        self.page_observers.remove(observer)

    def change_page(self, page: PageEnum):
        self.state.current_page = page
        self._notify_page(page)

    def _notify_page(self, page: PageEnum):
        for observer in self.page_observers:
            observer(page)

from tkinter.ttk import Button, Frame
from typing import TYPE_CHECKING

from sclick.enums import PageEnum

if TYPE_CHECKING:
    from sclick.controllers.app_controller import AppController
    from sclick.models.app_model import AppModel


class EntryPage:
    def __init__(self, frame: Frame, controller: "AppController", model: "AppModel") -> None:
        self.frame = Frame(frame)
        self.model = model
        self.controller = controller
        self.frame.grid(row=0, column=0)

        Button(self.frame, text="Load", command=self.handle_load_button_press).grid(column=0, row=0)
        Button(self.frame, text="Create", command=self.handle_create_button_press).grid(column=0, row=1)

    def handle_load_button_press(self) -> None:
        self.controller.change_page(PageEnum.LOAD)

    def handle_create_button_press(self) -> None:
        self.controller.change_page(PageEnum.CREATE)

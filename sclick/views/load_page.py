from tkinter.ttk import Button, Frame
from typing import TYPE_CHECKING

from sclick.enums import PageEnum

if TYPE_CHECKING:
    from sclick.controllers.app_controller import AppController
    from sclick.models.app_model import AppModel


class LoadPage:
    def __init__(self, frame: Frame, controller: "AppController", model: "AppModel") -> None:
        self.frame = Frame(frame)
        self.model = model
        self.controller = controller
        self.frame.grid()

        Button(self.frame, text="Back", command=self.handle_back_button_press).grid(column=0, row=0)

    def handle_back_button_press(self) -> None:
        self.controller.change_page(PageEnum.ENTRY)

from typing import TYPE_CHECKING

from tkinter import Tk
from tkinter.ttk import Frame

# from sclick.views.base import View
from sclick.enums import PageEnum
from sclick.views.create_page import CreatePage
from sclick.views.entry_page import EntryPage
from sclick.views.load_page import LoadPage

if TYPE_CHECKING:
    from sclick.controllers.app_controller import AppController
    from sclick.models.app_model import AppModel


class AppView:
    def __init__(self, controller: "AppController", model: "AppModel") -> None:
        self.controller = controller
        self.model = model
        self.model.register_page_observer(self.page_changed)

        # Configure root
        self.root = Tk()
        self.root.title = "Sclicker"
        self.root.resizable(False, False)
        self.root.attributes("-topmost", True)

        # Configure main frame
        self.frame = Frame(self.root, padding=10)
        # TODO: is this necessary? check
        self.frame.grid()

        self.current_page = None

    def run(self):
        self.root.mainloop()

    def page_changed(self, page: PageEnum):
        self.frame.destroy()
        self.frame = Frame(self.root, padding=10)
        self.frame.grid()
        match page:
            case PageEnum.ENTRY:
                self.current_page = EntryPage(self.frame, self.controller, self.model)
            case PageEnum.CREATE:
                self.current_page = CreatePage(self.frame, self.controller, self.model)
            case PageEnum.LOAD:
                self.current_page = LoadPage(self.frame, self.controller, self.model)

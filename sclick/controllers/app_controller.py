from sclick.enums import PageEnum
from sclick.models.app_model import AppModel
from sclick.views.app import AppView


class AppController:
    def __init__(self, model: AppModel) -> None:
        self.model = model
        self.view = AppView(self, self.model)

    def change_page(self, page: PageEnum) -> None:
        self.model.change_page(page)

    def run(self) -> None:
        self.change_page(PageEnum.ENTRY)
        self.view.run()

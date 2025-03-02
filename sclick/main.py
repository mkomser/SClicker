from sclick.controllers.app_controller import AppController
from sclick.models.app_model import AppModel


def main():
    app_model = AppModel()
    controller = AppController(app_model)
    controller.run()


if __name__ == "__main__":
    main()

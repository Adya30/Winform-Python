import sys
from PyQt6.QtWidgets import QApplication

from model.user import UserModel
from controller.auth import LoginController, RegisterController
from view.login_view import LoginView

def main():

    app = QApplication(sys.argv)
    user_model = UserModel()
    login_controller = LoginController(user_model)
    register_controller = RegisterController(user_model)
    login_view = LoginView(login_controller, register_controller)
    login_view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

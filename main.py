import sys
from PyQt6.QtWidgets import QApplication

# Model
from model.user import UserModel

# Controller
from controller.auth import LoginController, RegisterController

# View
from view.login_view import LoginView


def main():

    # inisialisasi aplikasi PyQt
    app = QApplication(sys.argv)

    # inisialisasi Model
    user_model = UserModel()

    # inisialisasi Controller
    login_controller = LoginController(user_model)
    register_controller = RegisterController(user_model)

    # inisialisasi View Login
    login_view = LoginView(
        login_controller,
        register_controller
    )

    # tampilkan window login
    login_view.show()

    # jalankan aplikasi
    sys.exit(app.exec())


# entry point program
if __name__ == "__main__":
    main()

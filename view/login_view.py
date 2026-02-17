from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QPixmap, QIcon, QGuiApplication, QColor
from PyQt6.QtCore import Qt
from view.popup import Popup


class LoginView(QWidget):

    def __init__(self, login_controller, register_controller):
        super().__init__()

        self.login_controller = login_controller
        self.register_controller = register_controller

        self.setWindowTitle("Login")
        self.resize(900, 500)
        self.setWindowIcon(QIcon("assets/icon.png"))

        self.center_window()
        self.init_ui()

    def center_window(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        frame = self.frameGeometry()
        frame.moveCenter(screen.center())
        self.move(frame.topLeft())

    def init_ui(self):

        main_layout = QHBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card = QFrame()
        card.setFixedSize(700, 400)
        card.setObjectName("card")

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(5)
        shadow.setColor(QColor(0, 0, 0, 80))
        card.setGraphicsEffect(shadow)

        # CARD LAYOUT
        card_layout = QHBoxLayout()
        card_layout.setContentsMargins(40, 40, 40, 40)
        card_layout.setSpacing(30)

        # IMAGE
        image_label = QLabel()
        pixmap = QPixmap("assets/icon.png")
        image_label.setPixmap(
            pixmap.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        )
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label.setStyleSheet("background-color: transparent;")

        # FORM
        form_layout = QVBoxLayout()
        form_layout.setSpacing(15)
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Login")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title.setStyleSheet("background-color: transparent;")

        subtitle = QLabel("Selamat Datang di Online Shop E-Commerce")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        subtitle.setStyleSheet("background-color: transparent;")

        # INPUT
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Username")
        self.input_username.setObjectName("input")

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Password")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setObjectName("input")

        # BUTTONS
        self.btn_login = QPushButton("Login")
        self.btn_login.setObjectName("login_button")
        self.btn_login.clicked.connect(self.handle_login)

        self.btn_register = QPushButton("Register")
        self.btn_register.setObjectName("register_button")
        self.btn_register.clicked.connect(self.open_register)

        # ADD WIDGETS TO FORM
        form_layout.addWidget(title)
        form_layout.addWidget(subtitle)
        form_layout.addSpacing(10)
        form_layout.addWidget(self.input_username)
        form_layout.addWidget(self.input_password)
        form_layout.addSpacing(10)
        form_layout.addWidget(self.btn_login)
        form_layout.addWidget(self.btn_register)

        # ADD TO CARD
        card_layout.addWidget(image_label)
        card_layout.addLayout(form_layout)
        card.setLayout(card_layout)

        # ADD CARD TO MAIN LAYOUT
        main_layout.addWidget(card)
        self.setLayout(main_layout)

        # APPLY STYLE
        self.setStyleSheet(self.load_styles())

    def load_styles(self):
        return """
        QWidget {
            background-color: #f5f7fb;
            font-family: Poppins;
        }
        QFrame#card {
            background-color: white;
            border-radius: 15px;
        }
        QLabel#title {
            font-size: 24px;
            font-weight: bold;
            color: #111;
        }
        QLabel#subtitle {
            font-size: 14px;
            color: #666;
        }
        QLineEdit#input {
            height: 40px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            padding-left: 10px;
            font-size: 14px;
        }
        QLineEdit#input:focus {
            border: 2px solid #4a90e2;
        }
        QPushButton#login_button {
            height: 40px;
            background-color: #4a90e2;
            color: white;
            border-radius: 8px;
            font-weight: bold;
        }
        QPushButton#login_button:hover {
            background-color: #357ABD;
        }
        QPushButton#register_button {
            height: 40px;
            background-color: transparent;
            color: #4a90e2;
            border: none;
            font-weight: bold;
        }
        QPushButton#register_button:hover {
            color: #357ABD;
        }
        """

    def handle_login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        try:
            user = self.login_controller.login_user(username, password)
            Popup(self, "Pemberitahuan", "Login berhasil")
        except Exception as e:
            Popup(self, "Peringatan", str(e))

    def open_register(self):
        from view.register_view import RegisterView
        self.register_window = RegisterView(self.register_controller, self.login_controller)
        self.register_window.show()
        self.close()


from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QPixmap, QIcon, QGuiApplication, QColor, QPainter, QPen
from PyQt6.QtCore import Qt, QPointF, QTimer
from PyQt6.QtWidgets import QApplication
from view.popup import Popup

def make_eye_icon(visible: bool) -> QIcon:

    size = 22
    px = QPixmap(size, size)
    px.fill(Qt.GlobalColor.transparent)

    painter = QPainter(px)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    pen = QPen(QColor("#888888"))
    pen.setWidth(2)
    painter.setPen(pen)

    cx, cy = size / 2, size / 2

    painter.drawArc(3, int(cy - 6), size - 6, 12, 0, 180 * 16)
    painter.drawArc(3, int(cy - 6), size - 6, 12, 180 * 16, 180 * 16)

    painter.setBrush(QColor("#888888"))
    painter.drawEllipse(QPointF(cx, cy), 3, 3)

    if not visible:
        painter.drawLine(4, size - 4, size - 4, 4)

    painter.end()

    return QIcon(px)

class LoginView(QWidget):

    def __init__(self, login_controller, register_controller):
        super().__init__()

        self.login_controller = login_controller
        self.register_controller = register_controller

        self.setWindowTitle("Login")

        self.setWindowFlags(
            Qt.WindowType.Window |
            Qt.WindowType.WindowCloseButtonHint |
            Qt.WindowType.WindowMinimizeButtonHint
        )

        self.setFixedSize(900, 500)

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

        # INPUT USERNAME
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Username")
        self.input_username.setObjectName("input")

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Password")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setObjectName("input")

        self.password_visible = False
        self.toggle_password_action = self.input_password.addAction(
            make_eye_icon(False),
            QLineEdit.ActionPosition.TrailingPosition
        )

        self.toggle_password_action.triggered.connect(
            self.toggle_password_visibility
        )

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

        card_layout.addWidget(image_label)
        card_layout.addLayout(form_layout)
        card.setLayout(card_layout)

        main_layout.addWidget(card)
        self.setLayout(main_layout)

        self.setStyleSheet(self.load_styles())

    def toggle_password_visibility(self):

        self.password_visible = not self.password_visible

        if self.password_visible:
            self.input_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.toggle_password_action.setIcon(make_eye_icon(True))
        else:
            self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.toggle_password_action.setIcon(make_eye_icon(False))

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

    def open_dashboard(self, user):
        if user["is_admin"]:
            from view.admin_view import AdminView
            self.admin_window = AdminView(
                self.login_controller,
                self.register_controller
            )
            self.admin_window.show()
        else:
            from view.customer_view import CustomerView
            self.customer_window = CustomerView(user)
            self.customer_window.show()

        self.close()


    def handle_login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        if not username.strip() or not password.strip():
            Popup(self, "Peringatan", "Username dan Password wajib diisi")
            return
        try:
            user = self.login_controller.login_user(username, password)

            Popup(self, "Pemberitahuan", "Login berhasil")

            QTimer.singleShot(900, lambda: self.open_dashboard(user))

        except Exception as e:
            Popup(self, "Peringatan", str(e))

    def open_register(self):
        from view.register_view import RegisterView
        self.register_window = RegisterView(self.register_controller, self.login_controller)
        self.register_window.show()
        self.close()
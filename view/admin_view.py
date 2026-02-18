from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from view.popup import popup_confirm_logout
from view.login_view import LoginView

class AdminView(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Dashboard")
        self.showMaximized()
        self.init_ui()

    def init_ui(self):

        # VERTICAL LAYOUT
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        header = QFrame()
        header.setFixedHeight(100)
        header.setStyleSheet("background-color: #2F3C8F;")

        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(40, 0, 50, 0)

        logo = QLabel()
        pixmap = QPixmap("assets/header.png") 

        logo.setPixmap(pixmap)
        logo.setScaledContents(True)
        logo.setFixedHeight(80)   
        logo.setFixedWidth(150)
        logo.setContentsMargins(35, 5, 0, 0)

        self.btn_tambah = QPushButton("Tambah Produk")

        header_layout.addWidget(logo)
        header_layout.addStretch()
        header_layout.addWidget(self.btn_tambah)

        header.setLayout(header_layout)

        # BODY
        body_layout = QHBoxLayout()
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        # SIDEBAR
        sidebar = QFrame()
        sidebar.setFixedWidth(260)
        sidebar.setStyleSheet("background-color: #2F3C8F;")

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        sidebar_layout.setSpacing(25)
        sidebar_layout.setContentsMargins(20, 60, 20, 20)

        menu_style = """
            QPushButton {
                background-color: white;
                color: #2F3C8F;
                border-radius: 20px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover {
                background-color: #e6e6e6;
            }
        """

        self.btn_produk = QPushButton("Produk")
        self.btn_pesanan = QPushButton("Pesanan")
        self.btn_riwayat = QPushButton("Riwayat")
        self.btn_profil = QPushButton("Profil")

        for btn in [
            self.btn_tambah,
            self.btn_produk,
            self.btn_pesanan,
            self.btn_riwayat,
            self.btn_profil
        ]:
            btn.setStyleSheet(menu_style)
            btn.setFixedHeight(45)

        sidebar_layout.addWidget(self.btn_produk)
        sidebar_layout.addWidget(self.btn_pesanan)
        sidebar_layout.addWidget(self.btn_riwayat)
        sidebar_layout.addWidget(self.btn_profil)
        sidebar_layout.addStretch()

        self.btn_logout = QPushButton("Logout")
        self.btn_logout.setFixedHeight(45)
        self.btn_logout.setStyleSheet("""
            QPushButton {
                background-color: #FF4B4B;
                color: white;
                border-radius: 22px;
                font-size: 16px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover {
                background-color: #e03d3d;
            }
        """)
        sidebar_layout.addWidget(self.btn_logout)
        sidebar.setLayout(sidebar_layout)

        # Hubungkan tombol ke method baru
        self.btn_logout.clicked.connect(self.logout)

        # CONTENT
        content = QFrame()
        content.setStyleSheet("background-color: #F4F6FB;")

        body_layout.addWidget(sidebar)
        body_layout.addWidget(content)

        main_layout.addWidget(header)
        main_layout.addLayout(body_layout)
        self.setLayout(main_layout)

    def logout(self):
        popup_confirm_logout(
            parent=self,
            message="Apakah Anda yakin ingin logout?",
            callback=self.goto_login
        )

    def goto_login(self):
        self.login_window = LoginView(None, None)
        self.login_window.show()
        self.close()
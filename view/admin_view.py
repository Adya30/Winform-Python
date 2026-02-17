from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,
    QFrame, QSizePolicy, QGridLayout
)
from PyQt6.QtGui import QIcon, QFont, QColor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsDropShadowEffect

class DashboardCard(QFrame):
    def __init__(self, title, value, subtitle):
        super().__init__()

        self.setObjectName("card")
        self.setFixedSize(250, 140)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout()

        title_label = QLabel(title)
        title_label.setObjectName("card_title")

        value_label = QLabel(value)
        value_label.setObjectName("card_value")

        subtitle_label = QLabel(subtitle)
        subtitle_label.setObjectName("card_subtitle")

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addWidget(subtitle_label)

        self.setLayout(layout)


class AdminView(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Admin Dashboard")
        self.resize(1200, 700)

        self.init_ui()
        self.setStyleSheet(self.load_styles())

    def init_ui(self):

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        sidebar = self.create_sidebar()
        content = self.create_content()

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)

        self.setLayout(main_layout)

    # SIDEBAR
    def create_sidebar(self):

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(250)

        layout = QVBoxLayout()

        # LOGO
        logo = QLabel("Tanamin")
        logo.setObjectName("logo")

        role = QLabel("Admin")
        role.setObjectName("role")

        layout.addWidget(logo)
        layout.addWidget(role)

        layout.addSpacing(30)

        # MENU BUTTONS
        layout.addWidget(self.menu_button("Katalog Produk"))
        layout.addWidget(self.menu_button("Data Pesanan"))
        layout.addWidget(self.menu_button("Riwayat Transaksi"))
        layout.addWidget(self.menu_button("Feedback"))
        layout.addWidget(self.menu_button("Pengaturan Akun"))

        layout.addStretch()

        sidebar.setLayout(layout)

        return sidebar

    def menu_button(self, text):
        btn = QPushButton(text)
        btn.setObjectName("menu_button")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        return btn

    # CONTENT AREA
    def create_content(self):

        content = QFrame()
        content.setObjectName("content")

        layout = QVBoxLayout()

        # CARDS
        card_layout = QHBoxLayout()

        card_layout.addWidget(
            DashboardCard("Total Produk", "156", "12% dari bulan lalu")
        )

        card_layout.addWidget(
            DashboardCard("Total Stok", "8,420", "5% dari bulan lalu")
        )

        card_layout.addWidget(
            DashboardCard("Total Produk", "156", "18% dari bulan lalu")
        )

        card_layout.addWidget(
            DashboardCard("Pendapatan Bulan Ini", "Rp 125.5 Juta", "25% dari bulan lalu")
        )

        layout.addLayout(card_layout)

        layout.addSpacing(20)

        # PANEL BAWAH
        bottom_layout = QHBoxLayout()

        big_panel = QFrame()
        big_panel.setObjectName("panel")
        big_panel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        small_panel = QFrame()
        small_panel.setObjectName("panel")
        small_panel.setFixedWidth(300)

        bottom_layout.addWidget(big_panel)
        bottom_layout.addWidget(small_panel)

        layout.addLayout(bottom_layout)

        content.setLayout(layout)

        return content

    def load_styles(self):
        return """

        QWidget {
            font-family: Poppins;
            background-color: #d8cbb7;
        }

        QFrame#sidebar {
            background-color: #f0f0f0;
            padding: 20px;
        }

        QLabel#logo {
            font-size: 24px;
            font-weight: bold;
        }

        QLabel#role {
            font-size: 14px;
            color: gray;
        }

        QPushButton#menu_button {
            background-color: #3fa847;
            color: white;
            padding: 12px;
            border-radius: 8px;
            text-align: left;
            font-size: 14px;
        }

        QPushButton#menu_button:hover {
            background-color: #2e7d32;
        }

        QFrame#content {
            padding: 20px;
        }

        QFrame#card {
            background-color: white;
            border-radius: 12px;
            padding: 15px;
        }

        QLabel#card_title {
            font-size: 14px;
            color: gray;
        }

        QLabel#card_value {
            font-size: 28px;
            font-weight: bold;
        }

        QLabel#card_subtitle {
            font-size: 12px;
            color: green;
        }

        QFrame#panel {
            background-color: white;
            border-radius: 12px;
        }

        """

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGraphicsDropShadowEffect, QPushButton
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor

class Popup(QWidget):
    def __init__(self, parent, title, message, success=True, duration=1000):
        super().__init__(parent)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(300, 120)
        self.duration = duration

        self.init_ui(title, message, success)
        self.center_over_parent(parent)

        self.show()

        QTimer.singleShot(self.duration, self.close)

    def center_over_parent(self, parent):
        geo = parent.geometry()
        x = geo.x() + (geo.width() - self.width()) // 2
        y = geo.y() + (geo.height() - self.height()) // 2
        self.move(x, y)

    def init_ui(self, title_text, message_text, success):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)

        card = QWidget()
        color = "#29C871" if success else "#E04444" 
        card.setStyleSheet(f"background-color: {color}; border-radius: 10px;")

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(5)
        shadow.setColor(QColor(0,0,0,120))
        card.setGraphicsEffect(shadow)

        layout = QVBoxLayout()
        layout.setContentsMargins(20,20,20,20)

        title = QLabel(title_text)
        title.setStyleSheet("font-weight:bold; font-size:16px; color:white;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        message = QLabel(message_text)
        message.setStyleSheet("font-size:14px; color:white;")
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(message)

        card.setLayout(layout)
        main_layout.addWidget(card)
        self.setLayout(main_layout)

def popup_success_login(parent, message, callback=None):
    popup = QWidget(parent)
    popup.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
    popup.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    popup.setFixedSize(300, 150)

    geo = parent.geometry()
    popup.move(geo.x() + (geo.width() - popup.width()) // 2,
               geo.y() + (geo.height() - popup.height()) // 2)

    layout = QVBoxLayout()
    layout.setContentsMargins(0,0,0,0)

    card = QWidget()
    card.setStyleSheet("background-color: #29C871; border-radius: 10px;")
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(20)
    shadow.setXOffset(0)
    shadow.setYOffset(5)
    shadow.setColor(QColor(0,0,0,120))
    card.setGraphicsEffect(shadow)

    card_layout = QVBoxLayout()
    card_layout.setContentsMargins(20,20,20,20)

    title = QLabel("Pemberitahuan")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title.setStyleSheet("font-size:16px; color:white;")
    card_layout.addWidget(title)

    msg = QLabel(message)
    msg.setAlignment(Qt.AlignmentFlag.AlignCenter)
    msg.setStyleSheet("font-size:14px; color:white;")
    msg.setWordWrap(True)
    card_layout.addWidget(msg)

    btn = QPushButton("Lanjut ke Login")
    btn.setStyleSheet("""
        QPushButton {
            background-color: white; color:#29C871; border-radius:5px; font-weight:bold; padding:5px;
        }
        QPushButton:hover { 
            background-color:#e6ffe6; 
        }
    """)
    def on_click():
        if callback:
            callback()
        popup.close()
    btn.clicked.connect(on_click)
    card_layout.addWidget(btn)

    card.setLayout(card_layout)
    layout.addWidget(card)
    popup.setLayout(layout)
    popup.show()
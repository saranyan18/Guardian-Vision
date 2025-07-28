from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont, QColor, QPalette, QMouseEvent
from PyQt5.QtCore import Qt

class TitleBar(QWidget):
    """
    Custom title bar: black background, neon title text, and a close button.
    Supports dragging the window by clicking and dragging this bar.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setFixedHeight(40)
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.Window, QColor("#000000"))
        self.setPalette(pal)

        # Title label
        self.title_label = QLabel("  Guardian Vision HUD", self)
        self.title_label.setFont(QFont("OCR A Extended", 16))
        self.title_label.setStyleSheet("color: #00ffea;")
        self.title_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        # Close button
        self.close_btn = QPushButton("✕", self)
        self.close_btn.setFixedSize(32, 32)
        self.close_btn.setFont(QFont("OCR A Extended", 16))
        self.close_btn.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: #ff0055;
                border: none;
            }
            QPushButton:hover {
                color: #ff0033;
            }
        """)
        self.close_btn.clicked.connect(self.on_close)

        # Layout for title bar
        h_layout = QHBoxLayout(self)
        h_layout.setContentsMargins(8, 0, 8, 0)
        h_layout.addWidget(self.title_label)
        h_layout.addStretch()
        h_layout.addWidget(self.close_btn)

        # Variables to support dragging
        self._drag_pos = None

    def on_close(self):
        if self.parent:
            self.parent.close()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._drag_pos:
            diff = event.globalPos() - self._drag_pos
            self.parent.move(self.parent.pos() + diff)
            self._drag_pos = event.globalPos()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self._drag_pos = None
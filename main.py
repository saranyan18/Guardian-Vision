import sys
from PyQt5.QtWidgets import QApplication
from app import WebcamApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebcamApp()
    window.show()
    sys.exit(app.exec_())

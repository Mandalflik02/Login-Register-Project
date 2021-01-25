import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QMessageBox, QDialog
from PyQt5.uic import loadUi


class Login(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Close the app",
            "Are tou sure you want to close the app?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            event.accept()
            print("close")
        else:
            event.ignore()
            print("don't close")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())

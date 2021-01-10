import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.login_func)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccountbutton.clicked.connect(self.go_to_create)

    def login_func(self):
        email = self.email.text()
        password = self.password.text()
        print("\nSuccessfully Logged in \nEmail: %s\nPassword: %s" % (email, password))

    def go_to_create(self):
        create_accoount = CreateAcount()
        widget.addWidget(create_accoount)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcount(QDialog):
    def __init__(self):
        super(CreateAcount, self).__init__()
        loadUi("createaccount.ui", self)
        self.singupbutton.clicked.connect(self.create_account_func)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def create_account_func(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            print(
                "\nSuccessfully Created account \nEmail: %s\nPassword: %s"
                % (email, password)
            )
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
login_window = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(login_window)
widget.setFixedWidth(450)
widget.setFixedHeight(500)
widget.show()
app.exec_()

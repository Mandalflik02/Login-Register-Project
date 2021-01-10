import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from user import User


u1 = User("naorfarjun@gmail.com", "1234567890")
u2 = User("naorfarjun", "naor2002")
users = []
users.append(u1)
users.append(u2)


def login_func(users, email, password):
    for user in users:
        if email == user.getEmail() and password == user.getPassword():
            return True, user
    return False, None


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("UI\login.ui", self)
        self.loginbutton.clicked.connect(self.login_func)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccountbutton.clicked.connect(self.go_to_create)

    def login_func(self):
        email = self.email.text()
        password = self.password.text()
        login_status, user = login_func(users, self.email.text(), self.password.text())
        if login_status == True:
            print(
                "\nSuccessfully Logged in \nEmail: %s\nPassword: %s" % (email, password)
            )
            main_page = MainPage(user)
            widget.addWidget(main_page)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_to_create(self):
        create_accoount = CreateAcount()
        widget.addWidget(create_accoount)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcount(QDialog):
    def __init__(self):
        super(CreateAcount, self).__init__()
        loadUi("UI\createaccount.ui", self)
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
            new_user = User(self.email.text(), self.password.text())
            users.append(new_user)


class MainPage(QDialog):
    def __init__(self, user):
        super(MainPage, self).__init__()
        loadUi("UI\main.ui", self)
        self.email.setText(user.getEmail())
        self.password.setText(user.getPassword())
        self.createdate.setText(user.getDate())
        self.logoutbutton.clicked.connect(self.logout_func)

    def logout_func(self):
        print("Logout of the system")
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

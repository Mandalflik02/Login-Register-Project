import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget
from PyQt5.uic import loadUi
from user import User

import socket
import threading

import random


HEADER = 1024
PORT = 5050
SERVER = "10.0.0.6"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MASSAGE = "!DISCONNECT!".encode(FORMAT)
AKS_FOR_NICKNAME = "NICK"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


u1 = User("naorfarjun@gmail.com", "naorfarjun", "1234567890")
u2 = User("1", "1", "1")
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

        # widget.setFixedWidth(450)
        # widget.setFixedHeight(500)

        # center the window
        self.to_the_center()

        self.singupbutton.clicked.connect(self.create_account_func)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def create_account_func(self):
        email = self.email.text()
        username = self.username.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()

            new_user = User(
                self.email.text(), self.username.text(), self.password.text()
            )
            users.append(new_user)
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            print(
                "\nSuccessfully Created account \nEmail: %s\nPassword: %s"
                % (email, password)
            )

    def to_the_center(self):
        # center the window
        qr1 = widget.frameGeometry()
        cp1 = QDesktopWidget().availableGeometry().center()
        qr1.moveCenter(cp1)
        widget.move(qr1.topLeft())


messages = []


class MainPage(QDialog):
    def get_message(self):
        while True:
            try:
                message = client.recv(HEADER).decode(FORMAT)
                msg_id = random.randint(0, 10000000)
                if message == AKS_FOR_NICKNAME:
                    client.send(self.user.getUsername().encode(FORMAT))
                    messages.append(msg_id)
                else:
                    if msg_id != messages[-1]:
                        self.chattextedit.append(f"{message}")
                        messages.append(msg_id)
            except:
                print("An error...")
                client.close()
                break

    def __init__(self, user):
        super(MainPage, self).__init__()
        loadUi("UI\main.ui", self)

        # set the window size
        # widget.setFixedWidth(1200)
        # widget.setFixedHeight(600)

        self.to_the_center()
        self.user = user
        self.detalisframe.setHidden(True)
        self.accountdetalisbutton.clicked.connect(self.show_detalis_func)
        self.accountdetalisbutton.setToolTip("Account Detalis")

        self.email.setText(user.getEmail())
        self.username.setText(user.getUsername())
        self.password.setText(user.getPassword())
        self.createdate.setText(user.getDate())
        self.logoutbutton.clicked.connect(self.logout_func)
        self.sendbutton.clicked.connect(self.send_message)
        get_thred = threading.Thread(target=self.get_message)
        get_thred.start()

    def send_message(self):
        message = "%s: %s" % (self.user.getUsername(), self.textsend.toPlainText())
        client.send(message.encode(FORMAT))

    def logout_func(self):
        print("Logout of the system")
        client.send(DISCONNECT_MASSAGE)
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # widget.setFixedWidth(450)
        # widget.setFixedHeight(500)
        self.to_the_center()

    def show_detalis_func(self):
        self.detalisframe.setHidden(not self.detalisframe.isHidden())

    def to_the_center(self):
        # center the window
        qr1 = widget.frameGeometry()
        cp1 = QDesktopWidget().availableGeometry().center()
        qr1.moveCenter(cp1)
        widget.move(qr1.topLeft())


app = QApplication(sys.argv)
login_window = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(login_window)
# widget.setFixedWidth(450)
# widget.setFixedHeight(500)
widget.show()
app.exec_()

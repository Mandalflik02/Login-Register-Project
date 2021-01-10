from datetime import datetime


class User:
    def create_date(self):
        cd = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return cd

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def getDate(self):
        return self.create_date

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.create_date = self.create_date()
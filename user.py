class User:
    def __init__(self, username, password):
        self.username = username
        self.password = Password_encryption(password)

    def Password_encryption(password):
        return password
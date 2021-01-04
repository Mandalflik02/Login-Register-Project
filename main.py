from user import User


def main():
    users = {"momo": "111"}

    users, register_status = register(users)
    if register_status == 1:
        print("New user added")
    else:
        print("Can't add new user")
    login_satus = login(users)
    print(login_satus)
    # for i in users.keys():
    # print("\nUsername: " + i + "\nPassword: " + users[i])


def register(users):
    print("\nREGIISTER")
    username = str(input("Enter username: "))
    password1 = str(input("Enter password: "))
    password2 = str(input("Enter password again: "))
    if username in users.keys():
        print("Username already in use")
        return users, 0
    if password1 != password2:
        print("The passwords do not match")
        return users, 0
    for key in users.keys():
        if password1 == users[key]:
            print("The password is already in use")
            return users, 0
    users[username] = password1
    return users, 1


def login(users):
    print("\nLOGIN")
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))
    for key in users.keys():
        if username == key:
            if password == users[key]:
                return "Login successfully"
    return "One or more of the data entered is incorrect"


main()
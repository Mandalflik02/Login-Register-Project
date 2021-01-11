import socket
import threading

import re
import string

HEADER = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MASSAGE = "!DISCONNECT!"
AKS_FOR_NICKNAME = "NICK".encode(FORMAT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []
nicknames = []


class DISCINNECT(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return "The username %s is Disconnect" % (self.username)


def broadcast(message):
    message = message.encode(FORMAT)
    for client in clients:
        client.send(message)


def hendla_client(client, addr):
    while True:
        try:
            message = client.recv(HEADER).decode(FORMAT)
            broadcast(message)
            if message == DISCONNECT_MASSAGE:
                index = clients.index(client)
                nickname = nicknames[index]
                raise DISCINNECT(nickname)
        except DISCINNECT as e:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat")
            print(e.__str__())
            nicknames.remove(nickname)
            break


def start():
    server.listen()
    print(f"[LISTEING] Server is listening on {SERVER}")
    while True:
        client, addr = server.accept()

        client.send(AKS_FOR_NICKNAME)
        nickname = client.recv(HEADER).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)
        print(f"[NEW CONNECTION] {addr} connected.\nNickname: {nickname}")
        broadcast(f"{nickname} join to the chat")
        client.send("Connected to the server!".encode(FORMAT))

        thread = threading.Thread(target=hendla_client, args=(client, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting....")
start()
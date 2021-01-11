import socket
import threading


HEADER = 1024
PORT = 5050
SERVER = "10.0.0.17"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MASSAGE = "!DISCONNECT!"
AKS_FOR_NICKNAME = "NICK"
NICKNAME = input("Enter a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def receive():
    while True:
        try:
            message = client.recv(HEADER).decode(FORMAT)
            if message == AKS_FOR_NICKNAME:
                client.send(NICKNAME.encode(FORMAT))
            else:
                print(message)
        except:
            print("An error...")
            client.close()
            break


def write():
    while True:
        message = f'{NICKNAME}: {input("::")}'
        client.send(message.encode(FORMAT))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

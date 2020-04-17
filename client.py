import socket
import time
from cryptography.fernet import Fernet

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 25565  # minecraft???

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        tcpsock.connect((HOST, PORT))
        break
    except ConnectionRefusedError:
        print('server unavailable, retrying')
        time.sleep(1)

key = tcpsock.recv(61)  # hardcoded keysize, this needs to change
print('connected to server, key: ' + str(key))

encryptor = Fernet(key)

while True:
    try:
        tosend = input('say something').encode()
        tcpsock.send(encryptor.encrypt(tosend))
    except ConnectionResetError:
        print('server disconnected')
        exit()

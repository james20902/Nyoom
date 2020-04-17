import socket
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = b"password"  # skip this entirely and hash by time?
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,  # this needs testing
    backend=default_backend())

f = Fernet(base64.urlsafe_b64encode(kdf.derive(password)))

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 25565  # minecraft???

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpsock.bind((HOST, PORT))
print('Awaiting connection at ' + HOST + ' with port ' + str(PORT))

tcpsock.listen()  # await connection

conn, addr = tcpsock.accept()

print('Connected by', addr)

while True:
    data = conn.recv(1024)

    if not data:
        break

    print(f.decrypt(data))

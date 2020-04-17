import socket
import os
import base64
import sys
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = b"password"  # skip this entirely and hash by time?
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=os.urandom(16),
    iterations=100000,  # this needs testing
    backend=default_backend())

key = base64.urlsafe_b64encode(kdf.derive(password))
print(sys.getsizeof(key))
f = Fernet(key)

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 25565  # minecraft???

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpsock.bind((HOST, PORT))
print('Awaiting connection at ' + HOST + ' with port ' + str(PORT))

tcpsock.listen()  # await connection

conn, addr = tcpsock.accept()

print('Connected by', addr)

conn.send(key)

while True:
    data = conn.recv(4096)  # decide size later based on how large packets will be

    if not data:
        break

    print('raw: ' + data.decode())
    print('decrypted: ' + f.decrypt(data).decode())

    # print(f.decrypt(data))

import socket
import time
from cryptography.fernet import Fernet

class Client:

    HOST = ''  # Standard loopback interface address (localhost)
    PORT = 0  # minecraft???
    key = b''
    encoder = 0

    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def validate(self, ip, port):
        try:
            self.tcpsock.connect((ip, port))
        except ConnectionRefusedError:
            return False
        self.key = self.tcpsock.recv(61)  # hardcoded keysize, this needs to change
        self.encoder = Fernet(self.key)
        self.HOST = ip
        self.PORT = port
        print('connected to server, key: ' + str(self.key))
        return True

    def send_message(self, content):
        try:
            self.tcpsock.send(self.encoder.encrypt(content.encode()))
        except ConnectionResetError:
            print('server disconnected')
            return False
        return True

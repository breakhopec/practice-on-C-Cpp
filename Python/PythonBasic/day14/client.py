import socket
from base64 import b64decode
from json import loads

client = socket.socket()
host = socket.gethostname()
port = 2333

client.connect((host, port))

print(client.recv(1024).decode('utf-8'))

data_recv = bytes()
data = bytes()

while True:
    data_recv = client.recv(1024)
    if not data_recv:
        break
    data += data_recv

pack = loads(data.decode('utf-8'))
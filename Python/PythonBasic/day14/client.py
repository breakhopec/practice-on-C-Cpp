import socket
from base64 import b64decode
from json import loads

client = socket.socket()
host = socket.gethostname()
port = 2333

client.connect((host, port))

print(client.recv(1024).decode('utf-8'))

data = bytes()

while True:
    data_recv = client.recv(1024)
    if not data_recv:
        break
    data += data_recv

pack = loads(data.decode('utf-8'))
with open('recv_' + pack['filename'], 'wb') as file_object:
    file_object.write(b64decode(pack['file']))
import socket
from base64 import b64encode
from json import dumps

server = socket.socket()
host = socket.gethostname()
port = 2333

server.bind((host, port))
server.listen(2)

with open('unravel.mp4', 'rb') as file_object:
    data = b64encode(file_object.read()).decode('utf-8')

pack = {}
pack['filename'] = 'unravel.mp4'
pack['file'] = data
json_str = dumps(pack)

while True:
    try:
        client, client_addr = server.accept()
        client.send('transfering video...'.encode('utf-8'))
        client.send(json_str.encode('utf-8'))
    except:
        pass
    finally:
        if client:
            client.close()
import socket
client = socket.socket()

host = '192.168.1.181'
port = 2333

client.connect((host, port))
client.close()
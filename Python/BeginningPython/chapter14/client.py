import socket
s = socket.socket()

con_host = socket.gethostname()
port = 2333

s.connect((con_host, port))
print(str(s.recv(1024), encoding='utf-8'))
print(str(s.recv(1024), encoding='utf-8'))
s.send(bytes(input(), encoding='utf8'))
print(str(s.recv(1024), encoding='utf-8'))
s.close()
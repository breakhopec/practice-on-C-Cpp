import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2333
server.bind((host, port))
server.listen(5)

print('server start!!')

while True:
    client, cli_addr = server.accept()
    print('received connection from: {}'.format(cli_addr))
    client.close()
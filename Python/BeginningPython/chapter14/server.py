import socket
server = socket.socket()

host = socket.gethostname()
port = 2333
server.bind((host, port))
server.listen(2)

while True:
    try:
        client, client_addr = server.accept()
        print('Got connection from: {}'.format(client_addr))
        client.send(b'thanks for you connection')
        client.send(b'are you Rinka? (Y/n)')
        response = str(client.recv(1), encoding='utf-8')
        if response.lower() == 'y':
            client.send(b'hi!')
        else:
            client.send(b'bye!')
        client.close()
    except ConnectionResetError:
        client.close()

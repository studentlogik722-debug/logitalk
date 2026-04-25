import socket
import threading

clients = []

def handle_client(current_client):
    while True:
        try:
            data = current_client.recv(1024)
            for client in clients:
                if client != current_client:
                    client.send(data)
        except:
            break
    clients.remove(current_client)
    current_client.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen()

print('Server ready')

while True:
    connection, client_address = server_socket.accept()
    clients.append(connection)

    threading.Thread(target=handle_client, args=(connection, client_address)).start()
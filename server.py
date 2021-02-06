import socket
import threading


CLIENTS = {}
SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 6969
MAX_CLIENTS = 5
MAX_COMMANDS = 100
 
 
def client_cmd():
    while True:
        client_send = input("Command for clients: ").encode("utf-8")
        for client in CLIENTS.values():
            client.send(client_send)


def client_recv(client_connection):
    # TODO handle on client disconnect.(hint: empty message for more details look at man/google)
    for _ in range(MAX_COMMANDS):
        data = client_connection.recv(2048)
        print(data.decode("utf-8"))


def register_new_clients():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_ADDRESS, SERVER_PORT))
    server.listen(MAX_CLIENTS)
    print("Server started")

    while True:
        client_connection, addr = server.accept()
        CLIENTS[client_connection.fileno()] = client_connection
        # TODO and how do you close your server?(hint thread.join())
        threading.Thread(target=client_recv, args=([client_connection])).start()
 s

def activate_server():
    threading.Thread(target=register_new_clients).start()
    client_cmd()


if __name__ == "__main__":
    activate_server()
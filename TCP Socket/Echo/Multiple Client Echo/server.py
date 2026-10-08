# Import Socket library
import socket as s 

#Import Threading Library
import threading as th

def handle_client(client):
    while True:
        data = client.recv(1024)   # receive data from client
        if (data == b""): break    
        client.sendall(data)    # send data back to client

# Define the Socket
server = s.socket(s.AF_INET, s.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))  # Bind the socket to port: 5000
server.listen()   # Make the Socket listen for client

while True:
    client, addr = server.accept()    # Accept the connection of a client
    print("Connected to a client", addr)
    th.Thread(target=handle_client, args=(client,)).start()   # Make a thread for multiple client

# Import Socket library 
import socket as s

# Define the socket 
server = s.socket(s.AF_INET, s.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))    # Bind the socket to port: 5000
server.listen()    # Make the Socket listen for client

# Connection to the Client
client, addr = server.accept()  # Accept the connection of a client
print("Connected to a client", addr)

while True:
    data = client.recv(1024)   # Receive the data from the client
    if (data == b""): break
    client.sendall(data)       # Send the data back to client
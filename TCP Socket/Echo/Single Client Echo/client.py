# Import Socket Library
import socket as s

# Define the Socket
client = s.socket(s.AF_INET, s.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))   # Connect to the server

while True:
    msg = input("> ")
    client.sendall(msg.encode())
    data = client.recv(1024)
    print(data.decode())
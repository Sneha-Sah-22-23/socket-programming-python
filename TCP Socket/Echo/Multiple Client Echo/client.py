# Import Socket library
import socket as s

# Define the Socket
client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))   # connect to the server at port: 5000

while True:
    msg = input("> ")
    client.sendall(msg.encode())    # send the message to server
    data = client.recv(1024)        # receive data from server
    print(data.decode())
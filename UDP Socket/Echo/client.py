# Import Socket Library
import socket as s

# Define the Socket
client = s.socket(s.AF_INET, s.SOCK_DGRAM)

while True:
    msg = input("> ")
    client.sendto(msg.encode(), ("127.0.0.1", 5000))  # send data to server on port: 5000
    data, addr = client.recvfrom(1024)   # receive data from server
    print(data.decode())   # Print the data received
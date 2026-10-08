# Import Socket Library
import socket as s 

# Define the Socket 
server = s.socket(s.AF_INET, s.SOCK_DGRAM)
server.bind(("127.0.0.1", 5000))   # Bind the socket to port: 5000

while True:
    data, addr = server.recvfrom(1024)   # Receive the data and address
    print("Data Sent by ", addr)
    server.sendto(data, addr)    # Send the data back to same address
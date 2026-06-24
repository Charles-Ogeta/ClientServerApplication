import socket

# Create client socket
client = socket.socket()

# Connect to server
client.connect(('127.0.0.1', 6000))

# Send message
client.send("Hello Server!".encode())

# Receive response
response = client.recv(1024).decode()

print("Server says:", response)

# Close connection
client.close()
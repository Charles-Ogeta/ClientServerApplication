import socket

# Create server socket
server = socket.socket()

# Bind to localhost and port 5000
server.bind(('127.0.0.1', 6000))

# Wait for connections
server.listen(1)

print("Server is waiting for connection...")

# Accept connection
conn, addr = server.accept()

print("Connected to:", addr)

# Receive message
message = conn.recv(1024).decode()

print("Client says:", message)

# Send response
conn.send("Hello Client, message received successfully!".encode())

# Close connection
conn.close()
server.close()
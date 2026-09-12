#import socket

#host_name = socket.gethostname()
#print(host_name)
#ip = socket.gethostbyname(host_name)
#print(ip)

#info = socket.getaddrinfo(host_name, port=443)
#print(info)

import socket

# Define the remote target server and port
HOST = "192.168.7.252"  # The server's hostname or IP address (e.g., 'localhost')
PORT = 22        # The specific TCP port to connect to

# 1. Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # 2. Establish the connection to the remote port
        s.connect((HOST, PORT))
        print(f"Successfully connected to {HOST}:{PORT}")
        
        # 3. Optional: Send data (must be encoded into bytes)
        s.sendall(b"Hello, Server!")
        
        # 4. Optional: Receive a response (up to 1024 bytes)
        response = s.recv(1024)
        print("Received:", response.decode("utf-8"))
        
    except ConnectionRefusedError:
        print(f"Connection refused. Is the server running on port {PORT}?")
    except socket.timeout:
        print("The connection attempt timed out.")

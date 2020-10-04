#!/usr/bin/env python3

"""
This is an example of an echo server. It echoes whatever it receives.
To test this echo server:
        - Find IP address of your machine by `ifconfig' on UNIX.
        - Then run `nc <IP address> 8000' to connect to this echo server.
        - Hit (Control-C) to terminate.
"""

import socket

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# If server shuts abruptly, make this socket reusable.
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpServer.bind(("0.0.0.0", 8000))

tcpServer.listen(2)

data = "temp"

print("Echo server in action..")

(client, (ip, port)) = tcpServer.accept()
print("Connected to %s:%s." %(ip, port))

while len(data):
    data = client.recv(2048)
    print("Received: %s" %(data.decode()), end='')
    client.send(data)

print("Terminating echo server..")

tcpServer.close()
client.close()

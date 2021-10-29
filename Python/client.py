#!/usr/bin/env python3

import sys
import socket

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enter self IP or 127.0.0.1 with port number (8000 in server.py)
tcpsock.connect((sys.argv[1], int(sys.argv[2])))

while True:
    try:
        userinput = input("Enter string: ")
        if len(userinput):
            tcpsock.send(userinput.encode())
            print("%s" %(tcpsock.recv(2048)))
        else:
            break
    except EOFError:
        print("\nNo input detected, closing socket.")
        break


tcpsock.close()

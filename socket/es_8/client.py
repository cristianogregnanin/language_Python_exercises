import socket
import sys

if len(sys.argv) != 5:
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(sys.argv[3].encode())
s.send(sys.argv[4].encode())

stringa = s.recv(1024).decode()

print(stringa)

s.close()
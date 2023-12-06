import socket
import sys
import os


if len(sys.argv) < 5 or not os.path.exists(sys.argv[1]):
    print("Errore negli argomenti <ip> <porta> <file>")
    exit()
PORT = int(sys.argv[3])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[2], PORT))
file = open(sys.argv[4], "r")
text = file.read()
s.send(text.encode())
str_reverse = s.recv(1024).decode()
print("Stringa reverse ricevuta dal server: ", str_reverse)
file.close()
s.close()
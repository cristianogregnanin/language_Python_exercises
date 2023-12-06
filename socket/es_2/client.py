import socket
import sys
import os

if len(sys.argv) != 4:
    print("Errore negli argomenti <ip> <porta> <file>")
    exit()
elif os.path.exists(sys.argv[3]) == False:
    print("Il file non esiste")
    exit()
PORT = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], PORT))
file = open(sys.argv[3], "r")
text = file.read()
s.send(text.encode())
str_reverse = s.recv(1024).decode()
print("Stringa reverse ricevuta dal server: ", str_reverse)
file.close()
s.close()
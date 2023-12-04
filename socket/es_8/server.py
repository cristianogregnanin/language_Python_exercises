#inverti stringa
import socket
import sys

if len(sys.argv) != 3:
    sys.exit(1)

def rimuovi_carattere(stringa, carattere):
    return stringa.replace(carattere, "")

HOST = sys.argv[1]
PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(6)

while 1:
    conn, addr = s.accept()
    stringa = conn.recv(1024).decode()
    
    carattere = stringa[-1]
    stringa = stringa[:-1]

    
    conn.send(rimuovi_carattere(stringa, carattere).encode())
    
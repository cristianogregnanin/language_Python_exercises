import socket
import sys

argv = sys.argv

if len(argv) != 5:
        print("Usage: python3 client.py <server-ip> <porta> <stringa> <carattere>")
        exit()

HOST = argv[1]
PORT = int(argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(argv[3].encode())
s.send(argv[4].encode())
stringa_ricevuta = s.recv(1024).decode()

print("Risultato: " + stringa_ricevuta) 
s.close
exit()
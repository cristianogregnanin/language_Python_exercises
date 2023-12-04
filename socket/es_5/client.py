import sys
import socket

argv = sys.argv
if len(argv) != 5:
    print("Errore nel passaggio parametri")
    sys.exit(1)

HOST = argv[1]
PORT = int(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(argv[3].encode())

rubricaOrdinata = s.recv(1024).decode()

file = open(argv[4], "w")
file.write(rubricaOrdinata)

s.close()

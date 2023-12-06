import socket
import sys

argv = sys.argv

if len(argv) != 4:
    print("Utilizzo: python server.py <indirizzo> <porta> <stringa>")
    sys.exit(1)

HOST = argv[1]
PORT = int(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(argv[3].encode())

strVocali = s.recv(1024).decode()
s.send(b"ok")
strConsonanti = s.recv(1024).decode()

print("\nStringa vocali: " + strVocali)
print("Stringa consonanti: " + strConsonanti)

s.close()

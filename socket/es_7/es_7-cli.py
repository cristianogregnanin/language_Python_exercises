import socket
import sys

argv = sys.argv

HOST = argv[1]  # ip
PORT = int(argv[2])  # porta
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # ci sono due parentesi perché è una tupla -> array di dati eterogeneo caratteristico di paython
stringa = argv[3]  # stringa
s.send(stringa.encode())
risp1 = s.recv(1024).decode()
risp2 = s.recv(1024).decode()
print(risp1 + "\n")
print(risp2)
s.close()

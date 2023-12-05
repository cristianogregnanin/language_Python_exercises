import socket 
import sys

argv = sys.argv
porta = int(argv[2])
indirizzo = argv[1]
stringa = argv[3]
carattere = argv[4]
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((indirizzo, porta))
server_socket.send(stringa.encode())
server_socket.send(carattere.encode())
stringa_nuova = server_socket.recv(1024)
print(stringa_nuova)


server_socket.close()
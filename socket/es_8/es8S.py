import socket 
import sys

def elimina_carattere(stringa, carattere):
    nuova_stringa = stringa.replace(carattere, '')
    return nuova_stringa

argv = sys.argv
porta = int(argv[1])
indirizzo = ""
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((indirizzo, porta))
server_socket.listen(10)
while 1:
        client_socket, client_address = server_socket.accept()
        stringa = client_socket.recv(1024).decode()
        carattere = client_socket.recv(1024).decode()
        stringa_nuova = elimina_carattere(stringa, carattere)
        client_socket.send(stringa_nuova.encode())


server_socket.close()
client_socket.close()

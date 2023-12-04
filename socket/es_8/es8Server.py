import socket
import sys

def rimuovi_carattere(stringa, carattere):
    return stringa.replace(carattere, '')


server_ip = sys.argv[1]
port = int(sys.argv[2])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, port))
server_socket.listen(5)


while True:
    client_socket, client_address = server_socket.accept()

    data = client_socket.recv(1024)
    stringa, carattere = data.split(',')

    risultato = rimuovi_carattere(stringa, carattere)

    client_socket.send(risultato.encode)

    client_socket.close()
    



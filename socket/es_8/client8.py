import socket
import sys


server_ip = sys.argv[1]
port = int(sys.argv[2])
stringa = sys.argv[3]
carattere = sys.argv[4]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, port))

data = f"{stringa},{carattere}"
client_socket.send(data.encode)

risultato = client_socket.recv(1024)
print(f"Risultato: {risultato}")

client_socket.close()



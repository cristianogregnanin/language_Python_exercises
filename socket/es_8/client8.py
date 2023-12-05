import socket
import sys
HOST=""
PORT= 50002
stringa=sys.argv[1]
carattere=sys.argv[2]
stringa_server = f"{stringa},{carattere}"
socket_client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((HOST,PORT))
socket_client.send(stringa_server.encode())
stringa_modificata= socket_client.recv(1024).decode()
print(f"Modified string received from server: {stringa_modificata}")
socket_client.close()

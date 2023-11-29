import socket
import sys
HOST = ""    
PORT = sys.argv[3]             
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
socket.send(sys.argv[1].encode())
socket.send(sys.argv[2].encode())
stringa2 = socket.recv(1024).decode()
print ('Server::. \t'+stringa2)
socket.close()
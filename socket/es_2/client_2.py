import socket
import sys

file_path = sys.argv[1]
with open(file_path, "r") as file:  # con il with non salva il percorso del file
    data = file.read()
HOST = ""
PORT = 5014

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))  # (( è una tupla))
invert = ""
print(data)


s.send(data.encode())
invert = s.recv(1024).decode()
print("Risposta del server::.\t" + invert)
file.close()
s.close()
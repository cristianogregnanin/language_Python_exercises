#inverti stringa
import socket
def inverti(data):
    return data[::-1]
HOST = ""              
PORT = 5014
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
while 1:
	conn, addr = s.accept()
	data = conn.recv(1024).decode()  
	invertita=inverti(data)
	conn.send(invertita.encode())
s.close()
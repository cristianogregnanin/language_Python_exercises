import socket
def Rimuove(s,c):
    return s.replace(c,'')
HOST=""
PORT= 50002
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((HOST,PORT))
socket_server.listen(10)
while 1:
    print("Server in ascolto...\t")
    connection,address= socket_server.accept()
    stringa= connection.recv(1024).decode()
    string, char = stringa.split(',')
    stringa_modificata = Rimuove(string, char)
    connection.sendall(stringa_modificata.encode())

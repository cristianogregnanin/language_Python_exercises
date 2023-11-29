import sys
import socket
HOST = ""               
PORT = sys.argv[1] 
vocali = ""
nvocali = ""         
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(6)
while 1:
    conn, addr = socket.accept()
    stringa = conn.recv(1024).decode()
    c=conn.recv(1024).decode()
    print ('Client',addr,'::. \t'+stringa)
    stringa2=stringa.replace(c,'')
    conn.send(stringa2.encode())
import os, socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 50000))
s.listen(10)
conn, addr = s.accept()

fd = os.open("f2.jpg", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0777)

while 1:
  
    buf = conn.recv(4096)
    if not buf: break
    os.write(fd,buf)

    
os.close(fd)
conn.close()

import socket,os,sys
HOST = ""               
PORT = sys.argv[1] 
vocali = ""
nvocali = ""         
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(6)
while 1:
    conn, addr = socket.accept()
    fd = conn.recv(1024).decode()
    

    conn.send(nvocali.encode())
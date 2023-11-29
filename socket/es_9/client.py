import socket,os
import sys
HOST = ""    
PORT = sys.argv[3]             
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
fd=os.open(sys.argv[1],os.O_RDONLY)
while 1:
    buf=os.read(fd,4096)
    if not buf:break
    socket.send(buf)
print("Server: %s"%(socket.recv(1024)).encode)
socket.close()

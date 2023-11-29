import sys
import socket
def consonanti(stringa):
    vocali = ""
    consonanti = ""
    for char in stringa:
        if char.lower() in "aeiou":
            vocali += char
        elif char.isalpha():
            consonanti += char
    return vocali, consonanti
HOST = ""               
PORT = 50000 
vocali = ""
nvocali = ""         
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(6)
while 1:
    conn, addr = socket.accept()
    stringa = conn.recv(1024).decode()
    print ('Client',addr,'::. \t'+stringa)
    vocali, nvocali=consonanti(stringa)
    conn.send(vocali.encode())
    conn.send(nvocali.encode())
import socket
import sys

argv = sys.argv

if(len(argv) != 5):
    print("Errore: numero argomenti errato!")
    sys.exit(0)

HOST = argv[1]   
PORT = int(argv[2])             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(argv[3].encode()) # mando la stringa
s.send(argv[4].encode()) # mando il carattere
stringa_senza_car = s.recv(1024).decode()
print (f"La stringa senza il carattere {argv[4]} è: {stringa_senza_car}\n")
s.close()
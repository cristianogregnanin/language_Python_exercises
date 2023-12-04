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
nome_file = argv[3]
s.send(nome_file.encode())
persone = s.recv(1024).decode()
persone_ordinate = persone.split(",")  # Divide la stringa ricevuta per ottenere la lista
with open(argv[4], "w") as file:
    for persona in persone_ordinate:
        file.write(persona + "\n")
file.close()
s.close()

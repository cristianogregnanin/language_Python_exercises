import socket
import sys
from classe_persona import Persona

argv = sys.argv

if(len(argv) != 2):
    print("Errore: numero argomenti errato!")

def dividi_persone(nome_file):
    for line in file:
        info = line.strip().split(" ")  # Divide la riga usando lo spazio come separatore
        if (len(info) == 3):  # Assicura che ci siano esattamente 3 parti (nome, cognome, telefono)
            nome, cognome, telefono = info
            persona = Persona(nome, cognome, telefono)
            persone.append(persona)


def ordina_persone(persone, persone_ordinate):
    persone_ordinate = persone.sort()



HOST = ""
PORT = int(argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(6)
while 1:
    conn, addr = s.accept()
    nome_file = conn.recv(1024).decode()
    persone = []
    persone_ordinate = []
    with open(nome_file, "r") as file:
        dividi_persone(nome_file)
    file.close()
    ordina_persone(persone, persone_ordinate)
    persone_ordinate_str = ",".join(persone_ordinate)  # così unisco tutte le persone in una sola stringa
    s.send(persone_ordinate_str.encode())
    conn.close()

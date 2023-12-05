import socket
import sys
from persona import Persona
def Divide():
    persone = []  # Creazione della lista di persone

    try:
        with open(nome_file, 'r') as file:  # Apre il file specificato in modalità di lettura
            for line in file:
                info = line.strip().split(" ")  # Divide la riga usando lo spazio come separatore
                if len(info) == 3:  # Assicura che ci siano esattamente 3 parti (nome, cognome, telefono)
                    nome, cognome, telefono = info
                    persona = Persona(nome, cognome, telefono)
                    persone.append(persona)  # Aggiunge l'oggetto Persona alla lista

    except FileNotFoundError:
        print(f"File {nome_file} non trovato.")

    return persone  # Restituisce la lista di persone create dal file
def Ordina(persone,persone_ordinate):
    persone_ordinate = persone.sort()  # Ordina la lista di persone per il campo 'nome'
HOST=""
PORT=50000
socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_server.bind((HOST,PORT))
socket_server.listen(10)
while 1:
    print("Server in ascolto...\t")
    connection, address = socket_server.accept()
    nome_file = connection.recv(1024).decode()
    persone = []
    persone_ordinate = []
    with open(nome_file, "r") as file:
        Divide(nome_file)
    file.close()
    Ordina(persone, persone_ordinate)
    persone_ordinate_str = ",".join(persone_ordinate)  # unisco tutte le persone in una sola stringa
    socket_server.send(persone_ordinate_str.encode())

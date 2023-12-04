import socket
import sys
import pickle
from Persona import Persona

def sort_rubrica(rubrica, persone):
    rubrica_linee = rubrica.split("\n")
    for riga in rubrica_linee:
        dati_persona = riga.split()    
        if len(dati_persona) >= 3:
            nome = dati_persona[0]
            cognome = dati_persona[1]
            telefono = dati_persona[2]
            persona = Persona(nome=nome, cognome=cognome, telefono=telefono)
            persone.append(persona)            
    # Ordina le persone per nome
    persone.sort(key=lambda x: x.nome)

argv = sys.argv
HOST = ""
PORT = int(argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

while 1:
    conn, addr = s.accept()    
    rubrica = conn.recv(1024).decode()
    persone = []
    sort_rubrica(rubrica, persone)
    for p in persone:
        print("Nome:", p.nome, "cognome:", p.cognome, "telefono:", p.telefono)
    #uso pickle.dumps per serializzare l'array persone in modo da poterlo inviare tramite socket
    conn.sendall(pickle.dumps(persone))
    conn.close()

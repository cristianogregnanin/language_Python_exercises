#inverti stringa
import socket
import sys

class Contato:
    def __init__(self, nome, cognome, numero_telefono):
        self.nome = nome
        self.cognome = cognome
        self.numero_telefono = numero_telefono
    def stampa(self):
        return self.nome + " " + self.cognome + " " + self.numero_telefono +"\n"

def popola(contati, rubrica):
    with open(rubrica, "r") as file:
        for line in file:
            data = line.split()
            contato = Contato(data[0], data[1], data[2])
            contati.append(contato)

def ordina(contati):
    contati.sort(key=lambda x: x.nome)

HOST = ""
PORT = int(sys.argv[1])
contati = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(6)

while 1:
    conn, addr = s.accept()
    data2 = ""
    data = conn.recv(1024).decode()
    popola(contati, data)
    ordina(contati)
    for contato in contati:
        data2 = contato.stampa()
        conn.send(data2.encode())

import sys
import socket


class Contatto:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono


def Ordina(rubrica):
    rubricaOrdinata = sorted(rubrica, key=lambda x: x.nome)
    return rubricaOrdinata


def Popola_Rubrica(file):
    rubrica = []
    contenuto = open(file, "r")
    for riga in contenuto:
        dati = riga.split()
        contato = Contatto(dati[0], dati[1], dati[2])
        rubrica.append(contato)

    return rubrica


argv = sys.argv
if len(argv) != 2:
    print("Errore nel passaggio parametri")
    sys.exit(1)

HOST = ""
PORT = int(argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

while 1:
    conn, addr = s.accept()

    file = conn.recv(1024).decode()
    rubrica = Popola_Rubrica(file)
    rubricaOrdinata = Ordina(rubrica)

    returnValue = ""
    for riga in rubricaOrdinata:
        returnValue += riga.nome + " " + riga.cognome + " " + riga.telefono + "\n"
    
    conn.send(returnValue.encode())
    conn.close()
s.close()

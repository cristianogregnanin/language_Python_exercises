import socket
import sys
import pickle
from persona import Persona  

def ordina(dati):
    persone = pickle.loads(dati)
    persone.sort()
    return pickle.dumps(persone)

HOST = sys.argv[1]
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(6)

while True:
    conn, addr = s.accept()
    print(f"Connection from {addr}")

    dati = conn.recv(100000)
    if not dati:
        break

    dati_ordinati = ordina(dati)
    conn.send(dati_ordinati)

    conn.close()

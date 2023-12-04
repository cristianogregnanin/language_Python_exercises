import socket
import sys

def invia_richiesta(indirizzo_server, porta_server, stringa_da_modificare, carattere_da_rimuovere):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((indirizzo_server, porta_server))

    dati = f"{stringa_da_modificare},{carattere_da_rimuovere}"
    client.send(dati.encode('utf-8'))

    risultato = client.recv(1024).decode('utf-8')
    print(f"Stringa modificata dal server: {risultato}")

    client.close()

if len(sys.argv) != 5:
    print("Utilizzo: python3 client.py <indirizzo-server> <porta> <stringa-da-modificare> <carattere-da-rimuovere>")
    sys.exit(1)

indirizzo_server = sys.argv[1]
porta_server = int(sys.argv[2])
stringa_da_modificare = sys.argv[3]
carattere_da_rimuovere = sys.argv[4]

invia_richiesta(indirizzo_server, porta_server, stringa_da_modificare, carattere_da_rimuovere)

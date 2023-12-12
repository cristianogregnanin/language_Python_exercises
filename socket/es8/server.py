import socket
import sys

def rimuovi_carattere(stringa, carattere):
    return stringa.replace(carattere, '')

if len(sys.argv) != 3:
    print("Errore, scrivi: server.py <server-ip> <porta>")
    exit()

HOST = sys.argv[1]
PORT = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)


while 1:
    conn, addr = s.accept()
    stringa = conn.recv(1024).decode()
    carattere = stringa[len(stringa)-1] #il carattere è in fondo alla stringa
    nuova_stringa = rimuovi_carattere(stringa, carattere)
    print(f"Stringa senza il carattere '{carattere}': {nuova_stringa}")
    conn.send(nuova_stringa.encode())
    conn.close()
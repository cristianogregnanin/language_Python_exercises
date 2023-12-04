import socket
import sys

argv = sys.argv

if (len(argv) != 3):
    print("Errore: numero argomenti errato!")
    sys.exit(0)


def togli_carattere(stringa, car):
    stringa_nuova = ""
    j = 0
    for i in range(len(stringa)):
        if (stringa[i] != car):
            stringa_nuova[j] = stringa[i]
            j = j + 1
    return stringa_nuova


HOST = argv[1]
PORT = int(argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(6)
while 1:
    conn, addr = s.accept()
    stringa = conn.recv(1024).decode()
    car = conn.recv(1024).decode()
    stringa = togli_carattere(stringa, car)
    conn.send(stringa.encode())
    conn.close()

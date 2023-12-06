import sys, socket, os


def rimuovi_carattere(stringa, carattere):
    return stringa.replace(carattere, "")


PORT = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("", PORT))
s.listen(10)

pid = os.fork()

while 1:
    
    if pid==0:
        conn, addr = s.accept()
    print("Ricevuta connessione da: ", addr)

    stringa = conn.recv(1024).decode()
    conn.send(str(len(stringa)).encode())
    carattere = conn.recv(1024).decode()
    print("\nStringa ricevuta: " + stringa)
    print("Carattere ricevuto: " + carattere)

    stringa = rimuovi_carattere(stringa, carattere)

    conn.send(stringa.encode())
    conn.close
    os._exit(0)
        
    


s.close()

import socket  
import sys
    
HOST = sys.argv[1]
PORT = int(sys.argv[2])
#creiamo socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
#effettuiamo una bind
try:
    s.bind((HOST, PORT))
except:
    print("Impossibile stabilire una connessione, utilizzare una porta diversa")
    exit()
s.listen(10)
while 1:
    #viene accettata la richiesta
    soa, conn = s.accept()
    #riceviamo la stringa
    stringa = soa.recv(1024).decode()
    #il carattere è inserito in coda alla stringa
    char = stringa[len(stringa)-1]
    #viene rimpiazzato il carattere con '' utilizzando la funzione replace
    str = stringa.replace(char, '')
    soa.send(str.encode())
    soa.close()
    

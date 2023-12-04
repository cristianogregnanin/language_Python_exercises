import socket
import sys

def main():
    if len(sys.argv) != 5:
        print("Argomenti insufficienti. Il programma deve essere invocato in questo modo: \n")
        print("python3 Client.py <Ip server> <Porta server> <stringa> <carattere da eliminare>\n")
        exit()
    #effettuiamo una connessione
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except:
        print("Connessione fallita")
        exit()
    #il carattere viene posto in coda alla stringa
    stringa = sys.argv[3] + sys.argv[4]
    #viene mandata la stringa al server
    s.send(stringa.encode())
    #viene ricevuta la stringa modificata
    stringa = s.recv(1024).decode()
    print("Stringa modificata: ", stringa)
    s.close()
    exit()
main()


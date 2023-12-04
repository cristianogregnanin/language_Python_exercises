import socket
import sys
import pickle #viene importata libreria pickle per  serializzare e deserializzare tipi di dato complessi come le liste

def main():
    if len(sys.argv) != 5:
        print("Argomenti insufficienti. Il programma deve essere invocato in questo modo: \n")
        print("python3 Client.py <Ip server> <Porta server> <File Rubrica> <Nuovo file rubrica ordinato>\n")
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
    #viene aperto il file in binario 
    file = open(sys.argv[3], 'rb') 
    #viene spedito il file al server
    s.sendfile(file)
    #viene ricevuto il file ordinato
    persone = s.recv(1024)
    #pickle gestisce la deserializzazione della lista
    persone = pickle.loads(persone)
    #viene chiuso mil file
    file.close()
    #viene aperto un nuovo file in scrittura
    file = open(sys.argv[4], 'w')
    for p in persone:
        #viene inserito ogni attributo della classe persona in una stringa unica e viene stampata
        line = p.nome + " " + p.cognome + " " + p.numero_telefono + '\n'
        file.writelines(str(line))
    #chiudiamo file e socket ed usciamo dal programma
    file.close()
    s.close()
    exit()
main()


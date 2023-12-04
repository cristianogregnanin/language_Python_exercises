import socket  
import sys
import persona #viene importata la classe Persona
import pickle #viene importata libreria pickle per  serializzare e deserializzare tipi di dato complessi come le liste

def SortList(file):
    file_line = "" #creiamo una stringa vuota che conterrà le singole linee del file
    lista_persone = [] #creiamo una lista vuota di persone
    #viene creato un ciclo che itera per l'intera lunghezza del file
    for i in range(len(file)):
        #se un carattere è diverso da newline allora viene sommato il carattere nella stringa file_line
        if file[i] != '\n':
            file_line += file[i]
        elif file[i] == '\n' and i < len(file) - 1:
            #se il carattere è uguale a newline e l'indice 'i' è minore della lunghezza del file -1 allora singifica che una riga è terminata e che il file non è ancora finito
            temp_array = file_line.split(' ') #temp_array contiene i 3 campi della persona ottenuti grazie ad uno split che divide in base a spazi vuoti
            p = persona.persona(temp_array[0], temp_array[1], temp_array[2]) #viene creato un oggetto di tipo persona
            lista_persone.append(p) #l'oggetto di tipo persona viene inserito nella lista di persone
            file_line = "" #la linea viene resettata
    #viene ordinata la lista grazie alla funzione lambda che permette di ordinare per attributo, in questo caso è in ordine alfabetico e ordina per chiave nome
    lista_persone.sort(key=lambda x: x.nome)
    #opzionale viene stampata la rubrica ordinata
    for p in lista_persone:
        print("Nome: ",p.nome, "Cognome: ", p.cognome, "Numero: ", p.numero_telefono)
    return lista_persone
    
    
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
    
    file = soa.recv(1024).decode()
    #richiamiamo la funzione SortLIst che restituisce la lista di persone
    lista_persone = SortList(file)
    #viene utilizzato pickle per serializzare la lista
    lista_persone = pickle.dumps(lista_persone)
    #viene mandata la lista al client
    soa.send(lista_persone)
    #chiusura socket accettata
    soa.close()
    

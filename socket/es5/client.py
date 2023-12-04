import socket
import sys
import pickle


if len(sys.argv) != 5:
    print("Utilizzo: python3 client.py <indirizzo_ip_server> <porta_server> <rubrica_file> <rubrica_ordinata_file>")
    sys.exit(1)

argv = sys.argv
HOST = argv[1]
PORT = int(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
percorso_file = argv[3]
rubrica_ordinata_file = sys.argv[4]

file = open(percorso_file, 'r')
rubrica = file.read()
s.send(rubrica.encode())
#ricevo dal server
rubrica_ordinata_data = s.recv(4096)
rubrica_ordinata = pickle.loads(rubrica_ordinata_data)
for p in rubrica_ordinata:
        print("Nome:", p.nome, "cognome:", p.cognome, "telefono:", p.telefono)

# Scrive la rubrica ordinata su un nuovo file
with open(rubrica_ordinata_file, 'w') as file2:
        for entry in rubrica_ordinata:
            file2.write(' '.join([str(entry.nome), str(entry.cognome), str(entry.telefono)]) + '\n')

s.close()


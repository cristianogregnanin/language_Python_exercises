import socket
import sys
import pickle
from persona import Persona  


server_ip = sys.argv[1]
port = int(sys.argv[2])
input_file = sys.argv[3]
output_file = sys.argv[4]

    
file = open("rubrica", 'r')
rubrica = [line.split() for line in file]
file.close()

persone = [Persona(nome, cognome, telefono) for nome, cognome, telefono in rubrica]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, port))

client_socket.send(pickle.dumps(persone))

data = client_socket.recv(100000)
persone_ordinate = pickle.loads(data)

file = open("rubricaout", 'w')
for persona in persone_ordinate:
    file.write(f"{persona.nome} {persona.cognome} {persona.telefono}\n")
file.close()

print(f"Rubrica ordinata salvata in {rubricaout.txt}")

    
client_socket.close()



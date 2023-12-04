import socket
import sys
if len(sys.argv)!=5:
    print("Numero di argomenti errato\t")
    sys.exit(1)
    
HOST=sys.argv[1]
PORT=int(sys.argv[2])
file=sys.argv[3]
#file_output=sys.argv[4]
socket_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_client.connect((HOST,PORT))
socket_client.send(file.encode())
people=socket_client.recv(1024).decode()
order_people=people.split(",")
#apro il mio file dove salvare i miei dati
with open(sys.argv[4],"w") as file2:
    for people in order_people:
        file2.write(people + "\n")
        file2.close()
socket_client.close()

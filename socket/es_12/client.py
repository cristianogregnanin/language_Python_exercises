import socket, sys, json


if len(sys.argv) < 6:
    print("Errore invocazione client")
    print(
        "uso: $ python3 client.py <server_ip> <porta> <numero_1> <numero_2> <operazione>"
    )
    exit()

HOST = sys.argv[1]
PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = {}
data["numero_1"] = sys.argv[3]
data["numero_2"] = sys.argv[4]
data["operazione"] = sys.argv[5]

json_data = json.dumps(data)

s.send(json_data.encode())

risultato = s.recv(32).decode()

print(
    f"Il risultato della {sys.argv[5]} fra {sys.argv[3]} e {sys.argv[4]} è: {risultato}"
)

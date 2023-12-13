import os, socket, sys, json


def somma(a, b):
    return a + b


def differenza(a, b):
    return a - b


if len(sys.argv) < 2:
    print("Errore invocazione server")
    print("uso: $ python3 server.py 32000")
    exit()

HOST = ""
PORT = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))

s.listen(10)


while 1:
    conn, addr = s.accept()
    pid = os.fork()
    if pid == 0:
        data = conn.recv(256).decode()
        json_data = json.loads(data)

        if json_data["operazione"] == "SOMMA":
            risultato = somma(int(json_data["numero_1"]), int(json_data["numero_2"]))

        elif json_data["operazione"] == "DIFFERENZA":
            risultato = differenza(
                int(json_data["numero_1"]), int(json_data["numero_2"])
            )
        else:
            risultato = "operazione non consentita"

        conn.send(str(risultato).encode())
        conn.close()

s.close()

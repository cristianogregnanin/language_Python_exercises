import socket, sys

if len(sys.argv) < 3:
    print("Errore negli argomenti <ip> <porta>")
    print("Esempio: $ python3 client.py libero.it 80 ")
    exit()

argv = sys.argv

HOST = argv[1]
PORT = int(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

http_request = "GET / HTTP/1.1\r\nHost:#{HOST}\r\n\r\n"

s.send(http_request.encode())

http_response = s.recv(4096).decode()
s.close

print(http_response)

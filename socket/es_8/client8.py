import socket
import sys

def send_data(s, data):
    bytes_sent = 0
    while bytes_sent < len(data):
        bytes_sent += s.send(data[bytes_sent:].encode())

def get_data(s):
    data = ""
    while True:
        packet = s.recv(4096)
        
HOST = sys.argv[1]
PORT = int(sys.argv[2])      
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
string = input("Inserisci una stringa")
char = input("inserisci un carattere")

send_data(s, f"{string},{char}")
modified_string = get_data(s)
print(f"stringa modificata: {modified_string}")

s.close()

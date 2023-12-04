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
s.listen(6)


while True:
    c, addr = s.accept()
    data = get_data(c)
    string, char = data.split(',')
    modified_string = string.replace(char, '')
    send_data(c, str(modified_string))
    c.close()

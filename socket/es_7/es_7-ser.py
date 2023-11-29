import socket
import sys


def cons_voc(stringa):
    voc = ["a", "e", "i", "o", "u"]
    cons = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    vocali = ""
    consonanti = ""
    for i in range(0, len(stringa)):
        if stringa[i] in voc:
            vocali += stringa[i]
        elif stringa[i] in cons:
            consonanti += stringa[i]
    return vocali, consonanti


argv = sys.argv

HOST = ""
PORT = int(argv[1])  # porta
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(6)
while 1:
    conn, addr = s.accept()
    stringa = conn.recv(1024).decode()
    voc, cons = cons_voc(stringa)
    risp1 = f"Vocali: {voc}"  # f sta per formatted string
    risp2 = f"Consonanti: {cons}"
    conn.send(risp1.encode())
    conn.send(risp2.encode())
    conn.close()

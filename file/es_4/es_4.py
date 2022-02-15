#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Contatto:
    def __init__(self, nome, cognome, numTelefonico):
        self.nome = nome
        self.cognome = cognome
        self.numTelefonico = numTelefonico

def Visualizza(rubrica):
    for contatto in rubrica:
        print("%s %s %s" %(contatto.nome, contatto.cognome, contatto.numTelefonico))
    return

def Aggiungi(rubrica):
    nome = input("Inserire il nome\n")
    cognome = input("Inserire il cognome\n")
    numeroTelefonico = input("Inserire il numero telefonico\n")
    for contatto in rubrica:
        if contatto.numTelefonico == numeroTelefonico:
            print("Errore, il numero inserito esiste gia'")
            return
    rubrica.append(Contatto(nome, cognome, numeroTelefonico))
    return

def Elimina(rubrica):
    numeroTelefonico = input("Inserire il numero telefonico\n")
    i = 0
    while i < len(rubrica):
        if rubrica[i].numTelefonico == numeroTelefonico:
            del rubrica[i]
            print("Il numero e' stato rimosso")
            return
        else: i += 1
    print("Il numero inserito non esiste nella rubrica")
    return

def Salva(rubrica):
    scelta = input("1) sovrascrivere il file originale\n2) salvare in un nuovo file\n")
    if scelta != '1' and scelta != '2':
        print("Errore, opazione invalida")
        return
    elif scelta == '1':
        f = open("rubrica.txt", 'w')
    else:
        nomeFile = input("Inserire il nome del file\n")
        f = open(nomeFile + ".txt", 'w')
    for contatto in rubrica:
        f.write(contatto.nome + " " + contatto.cognome + " " + contatto.numTelefonico + "\n")
    f.close()
    return

rubrica = []
f = open("rubrica.txt", 'r')
while True:
    line = f.readline()
    if line != "":
        rubrica.append(Contatto(line.split()[0], line.split()[1], line.split()[2]))
    else:
        f.close()
        break

while True:
    print("1) mostrare la rubrica a video")
    print("2) aggiungere un contatto alla rubrica")
    print("3) eliminare un contatto dalla rubrica dopo averlo ricercato con il suo numero di telefono")
    print("4) salvare la rubrica")
    x = input()
    if x == '1':
        Visualizza(rubrica)
    elif x == '2':
        Aggiungi(rubrica)
    elif x == '3':
        Elimina(rubrica)
    elif x == '4':
        Salva(rubrica)
        break
    else:
        print("Errore, opazione invalida")
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''Si crei un programma che nel momento dell'esecuzione popoli l'array
argv[] con una serie di numeri. Esempio: $ ./a.out 1 5 9 6
Il programma deve quindi chiedere in input un numero e deve cercarlo 
all'interno dell'array argv.
Se il numero è presente il programma deve dare un messaggio positivo
e deve mostrare la posizione dell'elemento, altrimenti deve stampare a 
video: "numero non presente"
Suggerimento: si usi una funzione per ricercare la posizione dell'
elemento. Tale funzione deve tornare la posizione oppure -1.'''

import sys 

argv = []

def Inserimento():
    for i in range(1, len(sys.argv)):
        argv.append(float(sys.argv[i]))

def Ricerca(argv, num):
    for i in range(0, len(argv) - 1):
        if(num == argv[i]):
            print("Il numero %d si trova alla posizione %d" %(num, i))
            break
        
while True:
    Inserimento()
    numb = int(input("Inserisci il numero da cercare: "))
    Ricerca(argv, numb)

    ripeti = input("Vuoi ripetere il programma? (y/n)\n")
    if(ripeti.lower() == "y"):
        continue
    else:
        break

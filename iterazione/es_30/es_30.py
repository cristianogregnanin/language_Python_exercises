#!/usr/bin/env python
#-*- coding: utf-8 -*- 

'''Dati due numeri interi positivi N1 e N2, verificare se N1 è il quadrato 
di N2. '''

while True:
    N1 = int(input("Inserisci N1 intero e positivo: "))
    N2 = int(input("Inserisci N2 intero,positivo e maggiore di N1: "))

    if(N1 < 0 or N2 < 0):
        print("Valori non inseriti correttamente")
        exit()
    else:
        if(pow(N1, 2) == N2):
            print("%d è il quadrato di %d" %(N2, N1))
        else:
            print("%d NON è la potenza di %d" %(N2, N1))
    
    risposta = int(input("Vuoi ripetere il programma?\nInserisci il numero dell'azione che vuoi effettuare\n1)Continua\n2)Esci\n"))
    if(risposta == 2):
        break
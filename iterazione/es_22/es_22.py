#!/usr/bin/env python
#-*- coding: utf-8 -*- 

'''Dato un numero N calcolare e visualizzare tutte le coppie di numeri che
danno per somma il numero stesso.'''

while True:
    N = int(input("Inserisci un numero intero e positivo: "))
    if(N < 0):
        print("Numero non valido")
        exit()
    else:
        for i in range(N):
            for j in range(N):
                if(i + j == N):
                    print("La somma tra %d e %d = %d" %(i, j, N))
    
    risposta = int(input("Vuoi ripetere il programma?\nInserisci il numero dell'azione che vuoi effettuare\n1)Continua\n2)Esci\n"))
    if(risposta == 2):
        break
            
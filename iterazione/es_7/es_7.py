'''Dato N un numero intero positivo maggiore di 1, generare e visualizzare
il numero precedente.'''

#!/usr/bin/env python
#-*- coding: utf-8 -*- 

while True:
    N = int(input("Inserisci un numero intero,positivo e maggiore di 1: "))

    if(N < 1):
        print("Numero non valido")
    else:
        print("Il numero precedente: %d" %(N-1))
    
    risposta = int(input("Vuoi ripetere il programma?\nInserisci il numero dell'azione che vuoi effettuare\n1)Continua\n2)Esci\n"))
    if(risposta == 2):
        break

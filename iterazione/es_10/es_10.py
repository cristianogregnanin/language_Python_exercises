'''Dato N un numero intero positivo, calcolare e visualizzare la somma dei
primi N numeri interi. '''

#!/usr/bin/env python
#-*- coding: utf-8 -*- 

while True:
    N = int(input("Inserisci un numero intero e positivo: "))

    if(N < 0):
        print("Numero non valido")
    else:
        num = 0
        cont = 0
        while(cont < N):
            num += cont
            cont += 1
        print("Il risultato della somma: %d" %(num))
    
    risposta = int(input("Vuoi ripetere il programma?\nInserisci il numero dell'azione che vuoi effettuare\n1)Continua\n2)Esci\n"))
    if(risposta == 2):
        break

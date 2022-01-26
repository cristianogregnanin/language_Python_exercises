#Dato N un numero intero positivo, generare e visualizzare in ordine
#crescente i numeri pari minori o uguali a N.

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

while True:
    N = int(input("Inserisci un numero intero e positivo: "))
    if(N < 0):
        print("Numero non valido")
    else:
        cont = 0
        while(cont <= N):
            if((cont % 2) == 0):
                print("%d = numero pari" %(cont))
            cont +=1
        
    risposta = int(input("Vuoi ripetere il programma?\nInserisci il numero dell'azione che vuoi effettuare\n1)Continua\n2)Esci\n"))
    if(risposta == 2):
        break

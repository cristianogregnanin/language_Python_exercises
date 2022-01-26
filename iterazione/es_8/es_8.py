'''Dato N un numero intero positivo, generare e visualizzare in ordine
decrescente i primi N numeri interi positivi.'''

#!/usr/bin/env python
#-*- coding: utf-8 -*- 

while True:
    N = int(input("Inserisci un numero intero e positivo: "))

    if(N < 0):
        print("Numero non valido")
    else:
        num = N
        print("I numeri in ordine decrescente sono: ")
        while(num > 0):
            print(num)
            num -=1
    
    risposta = int(input("Vuoi ripetere il programma?\nInserisci il numero dell'azione che vuoi effettuare\n1)Continua\n2)Esci\n"))
    if(risposta == 2):
        break
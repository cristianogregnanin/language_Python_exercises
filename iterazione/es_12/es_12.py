'''Dato N un numero intero positivo, calcolare e visualizzare la
somma dei primi N numeri pari.
'''

#!/usr/bin/env python
#-*- coding: utf-8 -*- 

while True:
    N = int(input("Inserisci un numero intero e positivo: "))

    if(N < 0):
        print("Numero non valido")
        exit()
    else:
        cont = 0
        sum = 0
        while(cont < N):
            if((cont % 2) == 0):
                sum += cont
            cont +=1

        print("La somma vale: %d" %(sum))
    
    risposta = int(input("Vuoi ripetere il programma?\nInserisci il numero dell'azione che vuoi effettuare\n1)Continua\n2)Esci\n"))
    if(risposta == 2):
        break

'''Dato N un numero intero positivo, calcolare e visualizzare la somma dei
primi N numeri dispari.'''

#!/usr/bin/env python
#-*- coding: utf-8 -*- 

N = int(input("Inserisci un numero intero e positivo: "))

if(N < 0):
    print("Numero non valido")
    exit()
else:
    cont = 0
    sum = 0
    while(cont < N):
        if((cont % 2) != 0):
            sum += cont
        cont +=1

    print("La somma vale: %d" %(sum))
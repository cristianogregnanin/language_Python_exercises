'''Dato N un numero intero positivo, calcolare e visualizzare la somma dei
primi N numeri interi. '''

#!/usr/bin/env python
#-*- coding: utf-8 -*- 

N = int(input("Inserisci un numero interoe positivo: "))

if(N < 0):
    print("Numero non valido")
    exit()
else:
    num = 0
    cont = 0
    while(cont < N):
        num += cont
        cont += 1
    print("Il risultato della somma: %d" %(num))

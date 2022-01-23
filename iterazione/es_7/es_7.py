'''Dato N un numero intero positivo maggiore di 1, generare e visualizzare
il numero precedente.'''

#!/usr/bin/env python
#-*- coding: utf-8 -*- 

N = int(input("Inserisci un numero intero,positivo e maggiore di 1: "))

if(N < 1):
    print("Numero non valido")
    exit()
else:
    print("Il numero precedente: %d" %(N-1))
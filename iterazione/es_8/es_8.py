'''Dato N un numero intero positivo, generare e visualizzare in ordine
decrescente i primi N numeri interi positivi.'''

#!/usr/bin/env python
#-*- coding: utf-8 -*- 

N = int(input("Inserisci un numero interoe positivo: "))

if(N < 0):
    print("Numero non valido")
    exit()
else:
    num = N
    print("I numeri in ordine decrescente sono: ")
    while(num > 0):
        print(num)
        num -=1
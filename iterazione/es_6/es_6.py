'''Dato N un numero intero positivo, generare e visualizzare in ordine
crescente i numeri compresi maggiori uguali di -N e minori uguali di N.
-N <= x <= N'''

#!/usr/bin/env python
#-*- coding: utf-8 -*- 

N = int(input("Inserisci un numero intero e positivo: "))

if(N < 0):
    print("Numero non valido")
    exit()
else:
    num = -N
    print("I numeri [%d, %d] sono: " %(num, N))
    while(num <= N):
        print(num)
        num += 1
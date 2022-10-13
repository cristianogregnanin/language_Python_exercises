'''Dato N un numero intero positivo, generato e visualizzato in ordine
crescente i numeri compresi maggiori uguali di -N e minori uguali di N.'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
N=0

while N<=0: N=int(input("Inserisci un numero intero positivo "))

print("i numeri interi, compresi nell'intervallo chiuso [",-N,",",N,"], in ordine crescente, sono:")

for N in range(-N,N+1):
    print(N)
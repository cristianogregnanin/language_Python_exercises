'''Dato un numero N(positivo)calcolare e visualizzare tutte le coppie di numeri che
danno per somma il numero stesso.
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

N=0
n1=0
n2=0

while N<=0:
    N=int(input("Inserisci un numero intero positivo "))

print("Coppie di numeri che hanno somma uguale a ",N)

for i in range(N):
    n1=i
    n2=N-n1
    print(n1,n2)


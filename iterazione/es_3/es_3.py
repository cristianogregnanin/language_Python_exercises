'''Dato N un numero intero positivo, generato e visualizzato in ordine crescente i numeri dispari
minori o uguali a N.'''

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

N=0
i=0

print("I numeri dispari minori o uguali a",N,",in ordine crescente, sono:")

while N<=0: N=int(input("Inserisci un numero intero positivo "))
while i<=N:
    if (i%2)!=0:
        print(i)
    i=i+1
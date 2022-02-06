'''Dato N un numero intero positivo, generato e visualizzato in ordine
crescente i numeri pari minori o uguali a N.'''

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

N=0
i=0

while n<=0: n=int(input("Inserisci un numero intero positivo "))
print("I numeri pari minori o uguali a",N,",in ordine crescente sono:")
while i<=n:
    if (i%2)==0:
        print(i)
    i=i+1

print(i)
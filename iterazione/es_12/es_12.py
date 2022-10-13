'''Dato N un numero intero positivo, calcolare e visualizzare la
somma dei primi N numeri pari.'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

N=0
i=0
sum=0

while N<=0: N=int(input("Inserisci un numero intero positivo "))
while i<N:
    if (i%2)==0:
        sum=sum+i
    i=i+1
print("La somma dei primi",N,"numeri interi positivi pari è: ",sum)
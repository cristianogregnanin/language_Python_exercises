'''Dato N un numero intero positivo, generato e visualizzato in ordine
decrescente i primi N numeri interi positivi.'''

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

N=0
i=0

while N<=0: N=int(input("Inserisci un numero intero positivo "))

i=N-1

print("I primi",N,"numeri interi positivi, in ordine decrescente, sono:")
while i>-1:
    print(i)
    i=i-1
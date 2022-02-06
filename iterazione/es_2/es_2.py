'''Dato N un numero intero positivo, generato e visualizzato in ordine crescente i primi N numeri
interi positivi.'''

#!/usr/bin/env python
# -*- coding: utf-8 -*- 


N=0
i=0


while N<=0: N=int(input("Inserisci un numero intero positivo "))

print("I primi",N,"numeri in ordine crescente sono:")

while i<N:
    print(i)
    i=i+1


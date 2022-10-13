'''Dati due numeri interi positivi N1 ed N2 calcola, tramite la somma
ripetuta, il prodotto dei due numeri e visualizzarli.'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

N1=0
N2=0
i=0
sum=0

while N1<=0: 
    N1=int(input("Inserisci un numero intero positivo "))
while N2<=0:
    N2=int(input("Inserisci un altro numero intero positivo "))

while i<N2:
    sum=sum+N1
    i=i+1
print("Il prodotto di",N1,"e",N2,"è",sum)

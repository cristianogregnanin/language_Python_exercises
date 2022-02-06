'''Dati due numeri interi e positivi N1 e N2 con N2>N1, genera e
visualizzato in ordine decrescente i numeri compresi tra N1 e N2.'''

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

N1=0
N2=0

while N1<=0: 
    N1=int(input("Inserisci un numero intero positivo "))
while N2<=N1:
    N2=int(input("Inserisci un altro numero intero positivo, maggiore del numero inserito precedentemente "))

i=N2

print("i numeri interi, compresi nell'intervallo chiuso [",N1,",",N2,"], in ordine decrescente, sono:")

while i>=N1:
    print(i)
    i=i-1


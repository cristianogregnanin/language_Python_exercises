'''Dati due numeri interi positivi N1 e N2 con N2>N1, generando e
visualizzare in ordine crescente i numeri interi compresi
nell'intervallo chiuso [N1,N2].'''

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

N1=0
N2=0

while N1<=0: 
    N1=int(input("Inserisci un numero intero positivo "))
while N2<=N1:
    N2=int(input("Inserisci un altro numero intero positivo, maggiore del numero inserito precedentemente "))

print("i numeri interi, compresi nell'intervallo chiuso [",N1,",",N2,"], in ordine crescente, sono:")

for numero in range(N1,N2+1):
    print(numero)



'''Dati due numeri interi positivi N1 ed N2 calcolare, mediante la somma
ripetuta, il prodotto dei due numeri e visualizzarli.'''

#!/usr/bin/env python
#-*- coding: utf-8 -*- 

N1 = int(input("Inserisci un numero intero e positivo: "))
N2 = int(input("Inserisci un numero intero e positivo: "))

if(N1 == 0 or N2 == 0):
    risultato = 0
    print("Il risultato = 0")
else:
    risultato = 0
    cont = 0
    while(cont < N2):
        risultato += N1
        cont += 1
    print("Il risultato: %d" %(risultato))

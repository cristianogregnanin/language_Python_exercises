#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    n1 = float(input("Inserisci n1: "))
    n2 = float(input("Inserisci n2: "))
    if float.is_integer(n1)==True and n1>0 and float.is_integer(n2)==True and n2>0:
        n1=int(n1)
        n2=int(n2)
        break
    print("Valori non accettabili. Requisiti:\nn1>0 n2>0 n1 e n2 interi")

prodotto = 0
for numeri in range(0, n2, 1):
    prodotto +=n1

print(prodotto)
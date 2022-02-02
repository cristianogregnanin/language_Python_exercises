#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    n = float(input("Inserisci un numero: "))
    if float.is_integer(n)==True and n>0:
        n=int(n)
        break
    print("Valori non accettabili. Requisiti: n>0 e intero")

for numeri in range(2,n): 
    if(n%numeri==0):
        print(f"{n} non è un numero primo")
        exit()
print(f"{n} è un numero primo")
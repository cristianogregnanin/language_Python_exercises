#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    n = float(input("Inserisci un numero: "))
    if float.is_integer(n)==True and n>1:
        n=int(n)
        break
    print("Valori non accettabili. Requisiti: n>1 e intero")

print(f"Il numero precedente di {n} è {n-1}")
#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    n = float(input("Inserisci un numero: "))
    if float.is_integer(n)==True and n>=0:
        n=int(n)
        break
    print("Valori non accettabili. Requisiti: n>=0 e intero")

ore=0
minuti=0
minuti=int(n/60)
secondi=n%60
ore=int(minuti/60)
minuti=minuti%60

print(f"{ore}h {minuti}m {secondi}s")
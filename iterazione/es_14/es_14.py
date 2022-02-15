#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    n1 = int (input("Inserire il primo numero positivo\n"))
    n2 = int (input("Inserire il secondo numero positivo\n"))
    if n1 < 0 or n2 < 0:
        print("Errore, i nueri inseriti non sono corretti")
    else: break

somma = 0
while n2 > 0:
    somma += n1
    n2 -= 1
print("Il prodotto dei due numeri vale %d" %somma)
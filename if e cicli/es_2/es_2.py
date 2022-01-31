#!/usr/bin/env python
# -*- coding: utf-8 -*-

somma = 0
while True:
    n1 = int(input("Inserire il primo numero\n"))
    n2 = int(input("Inserire il secondo numero\n"))
    prodotto = n1 * n2
    somma += prodotto
    if prodotto == 0: break

print("La somma dei prodotti vale %d" %(somma))
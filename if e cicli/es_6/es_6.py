#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    min = int(input("Inserire l'estremo sinistro dell'intervallo\n"))
    max = int(input("Inserire l'estremo destro dell'intervallo\n"))
    if max <= min:
        print("Errore, il massimo dev'essere strettamente maggiore del minimo")
    else: break

somma = 0
qtaNum = 0
while True:
    num = int(input("Inserire un numero intero\n"))
    somma += num
    qtaNum += 1

    if num < min or num > max:
        media = float(somma / qtaNum)
        print("La media dei numeri inseriti è %f" % media)
        break
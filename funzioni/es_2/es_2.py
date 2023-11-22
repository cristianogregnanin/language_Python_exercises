#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Si crei un programma che nel momento dell'esecuzione popoli l'array
# argv[] con una serie di numeri. Esempio: $ python3 es2.py 1 5 9 6
# Il programma deve calcolare la media dei numeri inseriti da riga di
# comando.
# Suggerimento: si usi una funzione per calcolare la somma dei numeri.
import sys

def media(array):
    somma = 0
    for i in range(1, len(array)):
        somma += int(array[i])
    return somma / (len(array)-1)

array = sys.argv
print("La media dei valori é: %f" % media(array))
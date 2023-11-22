#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Si crei un programma che nel momento dell'esecuzione popoli l'array
# argv[] con una serie di numeri. Esempio: $ python3 es_2.py 1 5 9 6
# Il programma deve calcolare la media dei numeri inseriti da riga di
# comando.
# Suggerimento: si usi una funzione per calcolare la somma dei numeri.


import sys


def media(arr):
    somma = 0
    for i in range(1, len(arr)):
        somma += int(arr[i])
    return somma / (len(arr)-1)

ar = sys.argv
if (len(ar) > 1):
    print("La media dei valori é: %f" % media(ar))
else:
    print("Argomenti del argv sbagliato")

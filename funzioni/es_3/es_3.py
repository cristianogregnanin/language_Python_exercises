#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Si crei un programma che nel momento dell'esecuzione popoli l'array
# argv[] con una serie di numeri. Esempio: $ python3 es3.py 1 5 9 6
# Il programma deve quindi chiedere in input un numero e deve cercarlo
# all'interno dell'array argv.
# Se il numero è presente il programma deve dare un messaggio positivo
# e deve mostrare la posizione dell'elemento, altrimenti deve stampare a
#video: "numero non presente"
# Suggerimento: si usi una funzione per ricercare la posizione dell'
# elemento. Tale funzione deve tornare la posizione oppure -1.

import sys

def ricerca(array, num):
    pos = -1
    for i in range(1, len(array)):
        if(int(array[i]) == num):
            pos = i
    return pos

array = sys.argv
num = int(input("Inserire un numero: "))
pos = ricerca(array, num)
if(pos != -1):
    print("Il numero %d é presente nell'array in posizione %d" % (num, pos))
else:
    print("Il numero %d non é presente nell'array" % num)
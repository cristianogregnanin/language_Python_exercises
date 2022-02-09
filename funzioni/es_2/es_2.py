#!/usr/bin/env python
# -*- coding: utf-8 -*-

def CalcoloMedia(array):
    somma = 0
    for num in array:   somma += num
    return somma/len(array)

while True:
    size = int(input("Indicare la lunghezza dell'array\n"))
    if size <= 0:
        print("Errore, valore inserito invalido")
    else:   break
array = [None] * size
i = 0
while i < size:
    array[i] = int(input("Inserire un numero\n"))
    i += 1
media = CalcoloMedia(array)
print("La media dei numeri inseriti vale %f" %media)
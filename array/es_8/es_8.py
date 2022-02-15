#!/usr/bin/env python
# -*- coding: utf-8 -*-

array = []
media = 0

while True:
    tmp = input("Inserire un numero. Digitare o Z per terminare l'inserimento.\n")
    if tmp == "z" or tmp == "Z": break
    else:
        array.append(float(tmp))
        media += float(tmp)

media /= len(array)
print("La media dei numeri inseriti e' %f" %media)

for number in array:
    if number > media: print(number)
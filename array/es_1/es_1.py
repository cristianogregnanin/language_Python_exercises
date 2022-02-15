#!/usr/bin/env python
# -*- coding: utf-8 -*-

array = [None] * 4
i = 0

while i < len(array):
    array[i] = int(input("Inserire un numero per popolare l'array\n"))
    i +=1
print("Adesso l'array e' popolato completamente")

print(array[::1])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

array = [None] * 10
i = 0
while i < len(array):
    array[i] = int(input("Inserire un numero intero\n"))
    i += 1

print("Pari")
for numer in array:
    if (numer % 2) == 0:
        print(numer)

print("Dispari")
for numer in array:
    if (numer % 2) == 1:
        print(numer)

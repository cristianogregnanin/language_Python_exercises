#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import I


while True:
    num = int(input("Inserire un numero intero positivo\n"))
    if num < 0:
        print("Errore, hai inserito un numero negativo")
    else: break

i = 0
while i <= num:
    print(i)
    i += 1
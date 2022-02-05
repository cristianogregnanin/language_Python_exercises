#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    num1 = int(input("Inserire il primo numero intero positivo\n"))
    num2 = int(input("Inserire il secondo numero intero positivo, dev'essere maggiore del primo\n"))
    if num1 < 0 or num2 < 0 or num2 <= num1:
        print("Errore, i numeri inseriti non sono corretti")
    else: break

num2 -= 1
while num2 > num1:
    print(num2)
    num2 -= 1
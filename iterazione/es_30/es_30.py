#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    num1 = int(input("Inserire il primo numero intero positivo\n"))
    num2 = int(input("Inserire il secondo numero intero positivo\n"))
    if num1 < 0 or num2 < 0:
        print("Errore, i numeri inseriti non sono corretti")
    else: break

if num1 == (num2 * num2):
    print("%d e' il quadrato di %d" %(num1, num2))
else:
    print("%d non e' il quadrato di %d" %(num1, num2))
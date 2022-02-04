#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    num = int(input("Inserire un numero intero strettamente positivo\n"))
    if num > 0: break
    else: print("Errore, hai inserito un numero sbagliato")

somma = 0
numCopia = num
while num > 0:
    somma += num
    num -= 1

print("La somma dei primi %d numeri interi vale %d" %(numCopia, somma))
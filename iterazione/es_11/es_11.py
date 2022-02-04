#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    num = int(input("Inserire un numero intero strettamente positivo\n"))
    if num > 0: break
    else: print("Errore, hai inserito un numero sbagliato")

dispari = 1
while dispari <= num:
    print(dispari)
    dispari += 2
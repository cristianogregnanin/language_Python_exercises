#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    num = int(input("Inserire un numero positivo\n"))
    if num < 0:
        print("Errore, hai inserito un numero negativo")
    else: break

dispari = 1
while dispari <= num:
    print(dispari)
    dispari +=2
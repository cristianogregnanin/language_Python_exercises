#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    num = int(input("Inserire un numero positivo\n"))
    if num < 0:
        print("Errore, hai inserito un numero negativo")
    else: break

pari = 0
while pari <= num:
    print(pari)
    pari +=2
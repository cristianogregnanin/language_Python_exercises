#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    num = int(input("Inserire un numero intero positivo\n"))
    if num < 0:
        print("Errore, hai inserito un numero negativo")
    else: break

divisore = 2
while divisore < num:
    if (num % divisore) == 0:
        print("%d non e' un numero primitivo" % num)
        break
    elif (divisore + 1) == num:
        print("%d e' un numero primitivo" % num)
    divisore += 1
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Leggere in input da tastiera due numeri maggiori di 0 e farne la somma.


def somma(n1, n2):
    return n1 + n2


while True:
    n1 = int(input("Inserire un primo numero: "))
    n2 = int(input("Inserire un secondo numero: "))

    if n1 > 0 and n2 > 0:
        break
    else:
        print("Devi inserire numero > di 0\n")


print("%d + %d = %d" % (n1, n2, somma(n1, n2)))

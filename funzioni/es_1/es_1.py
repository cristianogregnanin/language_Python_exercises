#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Leggere in input da tastiera due numeri maggiori di 0 e farne la somma.

def somma(n1, n2):
    return n1 + n2

n1 = int(input("Inserire un primo numero: "))
while n1 < 1:
    n1 = int(input("Numero inserito non maggiore di 0, rinserisci: "))

n2 = int(input("Inserire un primo numero: "))
while n2 < 1:
    n2 = int(input("Numero inserito non maggiore di 0, rinserisci: "))

print("%d + %d = %d" % (n1, n2, somma(n1, n2)))

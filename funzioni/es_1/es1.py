#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Leggere in input da tastiera due numeri maggiori di 0 e farne la somma.

def somma(n1, n2):
    return n1 + n2

n1=-1
n2=-2
while(n1 <0):
    n1=int(input("Inserire un primo numero: "))
    if(n1<0):
        print("Inserire solo numeri maggiori di 0")
while(n2<0):
    n2 = int(input("Inserire un secondo numero: "))
    if(n2<0):
        print("Inserire solo numeri maggiori di 0")

print("%d + %d = %d" % (n1, n2, somma(n1, n2)))

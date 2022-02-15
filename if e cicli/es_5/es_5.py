#!/usr/bin/env python
# -*- coding: utf-8 -*-

pari = 0
dispari = 0
nullo = 0

while True:
    n1 = int(input("Inserire il primo numero\n"))
    n2 = int(input("Inserire il secondo numero\n"))
    n3 = int(input("Inserire il terzo numero\n"))

    if n1-n2 == 0:
        nullo += 1
    elif (n1-n2) % 2 == 1:
        dispari += 1
    else:
        pari += 1

    if (n1 + n2) < n3:
        print("La differenza tra A e B è stata %d volte pari, %d volte dispari, %d volte nulla" %(pari, dispari, nullo))
        break
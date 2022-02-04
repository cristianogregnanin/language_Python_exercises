#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = int(input("Inserire un numero positivo\n"))

if num > 0:
    num += 1
    print("Il numero successivo e' %d" % num)
else:
    print("Errore, hai inserito un numero negativo o nullo")
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import math

somma = 0
while True:
    num = float(input("Inserire un numero reale\n"))
    if num >= 0:
        somma += math.sqrt(num)
    else:
        print("Errore, hai inserito un numero negativo. La somma delle radici vale %f" %somma)
        break
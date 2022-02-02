#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

while True:
    n1 = float(input("Inserire il primo numero reale\n"))
    n2 = float(input("Inserire il secondo numero reale\n"))

    if n1 == 0 and n2 == 0:
        print("Impossibile calcolare il rapporto tra due zeri")
        break
    
    elif (n1 >= n2 and n2 == 0) or (n2 >= n1 and n1 == 0):
        print("Impossibile effettuare la divisione col divisore pari a 0")
        break
    
    else:
        if n1 >= n2 :
            rapporto = n1/n2
        else:
            rapporto = n2/n1

    if rapporto >= 0:
        radice = math.sqrt(rapporto)
        print(radice)
    else:
        print("Impossibile estrarre la radice quadrata di un numero negativo")
        break
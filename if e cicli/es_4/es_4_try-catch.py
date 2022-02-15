#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
while True:
    n1 = float(input("Inserire il primo numero reale\n"))
    n2 = float(input("Inserire il secondo numero reale\n"))
    #sebbene il try-chatch agevoli il coding, personalmente ritengo che sia
    #opportuno usare gli if-else per gestire le eccezioni prevedibili, e
    #il try-chatch con quelli imprevedibili come il dialogo con risorse esterne
    try:
        if n1 >= n2 :
            rapporto = n1/n2
        else:
            rapporto = n2/n1
    except ArithmeticError:
        print("Impossibile effettuare la divisione col divisore pari a 0")
        break
    
    if rapporto >= 0:
        radice = math.sqrt(rapporto)
        print(radice)
    else:
        print("Impossibile estrarre la radice quadrata di un numero negativo")
        break

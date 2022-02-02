#!/usr/bin/env python
#-*- coding: utf-8 -*-

numero=int(input("Inserisci un valore intero di N\n"))

while numero<0:
    numero=int(input("Il numero deve essere intero\n"))

contatore=0

while contatore<=numero:
    if contatore%2==0:       
        contatore= contatore +1
    else:
        print (contatore)
        contatore=contatore +1


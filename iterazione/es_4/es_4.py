#!/usr/bin/env python
#-*- coding: utf-8 -*-

numero=int(input("Inserisci un valore intero di N\n"))
contatore=1
while contatore<=numero:
    if contatore%2==0:      
        print (contatore) 
        contatore= contatore +1
    else:
        contatore=contatore +1
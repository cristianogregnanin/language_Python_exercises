#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Leggere in input da tastiera due numeri maggiori di 0 e farne la somma. 

def leggi():
    N1 = int(input("Inserisci il primo numero: "))
    N2 = int(input("Inserisci il secondo numero: "))

    print("La somma vale: %d" %(N1+N2))

leggi()
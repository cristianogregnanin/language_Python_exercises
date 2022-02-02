#!/usr/bin/env python
#-*- coding: utf-8 -*-

n1=int(input("Inserisci un valore intero di N1\n"))
n2=int(input("Inserisci un valore intero di N2\n"))

if(n1>n2):
    exit()

contatore=n2
while contatore>=n1:
    print (contatore)
    contatore=contatore-1

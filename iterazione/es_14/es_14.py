#!/usr/bin/env python
#-*- coding: utf-8 -*-

n1=int(input("Inserisci un valore intero di N1\n"))
n2=int(input("Inserisci un valore intero di N2\n"))

somma=0

if(n1<0|n2<0):
    exit()

while n2!=0:
    somma=somma+n1
    n2=n2-1

print("\n",somma)


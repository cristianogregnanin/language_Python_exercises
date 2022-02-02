#!/usr/bin/env python
#-*- coding: utf-8 -*-

n=int(input("Inserisci un valore intero di N\n"))
if(n<0):
    exit()

somma=0

while n>0:
    if(n%2==0):
        somma=somma+n
        n=n-1
    else:
        n=n-1
print(somma)

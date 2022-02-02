#!/usr/bin/env python
#-*- coding: utf-8 -*-

n1=int(input("Inserisci un valore intero di N1\n"))
if(n1<0):
    exit()
n2= -n1

while n2<=n1:
    print ("\n",n2)
    n2=n2+1

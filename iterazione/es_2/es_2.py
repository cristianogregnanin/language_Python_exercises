#!/usr/bin/env python
#-*- coding: utf-8 -*-

numero=int(input("Inserisci un valore intero di N\n"))
div=2
divisori=0
while numero>div and numero%div==0 :
    divisori=divisori+1
    div=div+1

if divisori==0:
    print("Il numero è un numero primo\n")
else:
    print("Il numero non è primo\n")



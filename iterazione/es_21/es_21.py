#!/usr/bin/env python
#-*- coding: utf-8 -*-

n=int(input("Inserisci il numero da analizzare\n"))

for i in range(2,n):
    if((n%i)==0):      
        print("n non è un numero primo") 
        break
    else:
        print("n è un numero primo")

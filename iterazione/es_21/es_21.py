#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

N=int(input("inserisci il numero da controllare\n"))
if(N<=0):
    print("numero non valido")
    exit()

for numero in range(2,N): 
    if(N%numero==0):
        print("%d non è un numero primo"%(N))
        exit()
print("%d è un numero primo"%(N))

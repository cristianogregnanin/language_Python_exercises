#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

N=int(input("inserisci un numero\n"))
if(N<=0):
    print("numero non valido")
    exit()

print()
for numero in range(0,N,1):
    print(numero)
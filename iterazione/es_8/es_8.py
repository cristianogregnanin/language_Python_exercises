#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

N=int(input("inserisci il primo numero\n"))
if(N<=0):
    print("Il numero deve essere positivo")
    exit()

print()
for numero in range(N,0,-1):
    print(numero)
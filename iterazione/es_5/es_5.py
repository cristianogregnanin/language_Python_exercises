#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

N1=int(input("inserisci il primo numero\n"))
N2=int(input("inserisci il secondo numero\n"))
if(N1>=N2):
    print("Il secondo numero deve essere maggiore del primo")
    exit()

print()
for numero in range(N1,N2+1,1):
    print(numero)
#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

N=int(input("inserisci il primo numero\n"))
if(N<=0):
    print("Il numero deve essere positivo")
    exit()

print()
somma=0
for numero in range(0,N+1,1):
    somma=somma+numero
   
print("somma= %d"% (somma) )
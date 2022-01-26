#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

N=int(input("inserisci un numero\n"))
if(N<0):
    print("numero non valido")
    exit()

print()
somma=0
for numero in range(0,N+1,2):
    somma= somma+numero
print("somma dei numeri pari = %d"%(somma) )
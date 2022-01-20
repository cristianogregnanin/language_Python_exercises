#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

N=int(input("inserisci un numero\n"))
if(N<=0):
    print("numero non valido")
    exit()

N2=N+1
print("Numero inserito=%d\nNumero incrementato=%d"%(N,N2))
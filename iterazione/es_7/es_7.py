#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

N=int(input("inserisci il primo numero\n"))
if(N<=1):
    print("Il numero deve essere positivo e maggiore di 1")
    exit()

print()
print("numero inserito= %d\nnumero precedente= %d"%(N,N-1))
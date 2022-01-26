#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

N1=int(input("inserisci il primo numero\n"))
N2=int(input("inserisci il secondo numero\n"))
if(N1<=0 or N2<=0):
    print("entrambi i numeri devono essere positivi")
    exit()

print()
prodotto=0
for numero in range(0,N2,1):
    prodotto=prodotto+N1
print("prodotto %d*%d=%d"%(N1,N2,prodotto))
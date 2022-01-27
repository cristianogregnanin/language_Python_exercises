#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

N1=int(input("inserisci il primo numero\n"))
N2=int(input("inserisci il secondo numero\n"))
if(N1<=0 or N2<=0):
    print("numeri non validi")
    exit()

if (N2**2==N1):
    print("%d è il quadrato di %d"%(N1,N2))
else:
    print("%d non è il quadrato di %d"%(N1,N2))


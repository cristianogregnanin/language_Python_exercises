#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

N=int(input("inserisci il numero\n"))
if(N<=0):
    print("numero non valido")
    exit()
print()
for numero in range(1,int(N/2)+1): 
    print("%d+%d"%(numero,N-numero))


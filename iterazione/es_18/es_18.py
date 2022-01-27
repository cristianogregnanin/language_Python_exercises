#!/usr/bin/env pyton
#-*- coding:utf-8 -*-

secondi=int(input("inserisci il numero di secondi\n"))
if(secondi<=0):
    print("numero non valido")
    exit()

ore=0
minuti=0

minuti=int(secondi/60)
secondi=secondi%60

ore=int(minuti/60)
minuti=minuti%60

print("%dH: %dm: %ds"%(ore,minuti,secondi))
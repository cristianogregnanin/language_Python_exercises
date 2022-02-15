#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    numSecondi = int(input("Inserire il numero dei secondi\n"))
    if numSecondi < 0:
        print("Errore, hai inserito un numero negativo")
    else: break

numOre = numSecondi // 3600
numSecondi = numSecondi % 3600
numMinuti = numSecondi // 60
numSecondi = numSecondi % 60
print("%dh %dm %ds" %(numOre, numMinuti, numSecondi))
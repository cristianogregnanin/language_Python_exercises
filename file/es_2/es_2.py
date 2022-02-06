#!/usr/bin/env python
# -*- coding: utf-8 -*-

array = []
i = 0
nomeVecchio = ""
etaVecchio = 0
while i < 5:
    nome = input("Inserire il nome della persona\n")
    eta = int(input("Inserire l'eta' della persona\n"))
    if eta > etaVecchio:
        etaVecchio = eta
        nomeVecchio = nome
    i += 1

f = open("vecchio.txt", 'w')
f.write(nomeVecchio + " " + str(etaVecchio))
f.close()

print("%s %d" %(nomeVecchio, etaVecchio))
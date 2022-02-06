#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Inversione(stringa):
    indexInvertito = len(stringa) - 1
    while indexInvertito >= 0:
        print("%c" %stringa[indexInvertito], end='')#stamapare la lettera senza new line
        if indexInvertito == 0: print("")#new line
        indexInvertito -= 1

stringa = input("Inserire una stringa\n")
Inversione(stringa)

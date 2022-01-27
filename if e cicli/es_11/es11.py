#!/usr/bin/env python
# -*- coding: utf-8 -*- 

n1 = (int)(input("Inserire un numero positivo intero maggiore di zero.\n"))

while n1 <= 0:
    print("Errore, riprova\n")
    n1 = (int)(input("Inserire un numero positivo intero maggiore di zero.\n"))

riga = 0
while riga < n1:
    colonna = 0
    while colonna < n1:
        if  riga != 0 and n1-riga != 1 and colonna != 0 and n1-colonna != 1:
            print(" ", end='')
        else:
            print("*", end='')
        colonna += 1

    riga += 1
    print("")

print("End")
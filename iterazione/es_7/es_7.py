#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    num = int(input("Inserire un numero intero positivo maggiore di uno\n"))
    if num <= 1:
        print("Errore, il numero inserito e' erratto")
    else: break

print("Il numero precedente di %d e' %d" %(num, num - 1))
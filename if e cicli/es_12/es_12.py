#!/usr/bin/env python
# -*- coding: utf-8 -*- 

n1 = int(input("Inserire il primo numero intero\n"))
n2 = int (input("Inserire il secondo numero intero\n"))

if n1 == 0 and n2 == 0: print("Errore, la potenza 0^0 non ha senso")
else : print("La potenza %d^%d vale %d" %(n1, n2, n1**n2))
'''Dati due numeri interi positivi N1 e N2, verificare se N1 è il quadrato
di N2.'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

N1=0
N2=0

while N1<=0: 
    N1=int(input("Inserisci un intero positivo N1 "))
while N2<=0:
    N2=int(input("Inserisci un altro numero intero positivo N2"))

if sqrt(N1)==N2:
    print("N1 è il quadrato di N2")
else:
    print("N1 non è il quadrato di N2")
'''Dato un numero intero positivo N verificare se N è un numero primo.'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

N=0

while N<=0:
    N=int(input("Inserisci un numero intero positivo "))

if N==2:
    print(N," è un numero primo")
else:
    if N%2==0:
        print(N," non è un numero primo")
    else:
        print(N," è un numero primo")


#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''Si crei un programma che nel momento dell'esecuzione popoli l'array
argv[] con una serie di numeri. Esempio: $ ./a.out 1 5 9 6
Il programma deve calcolare la media dei numeri inseriti da riga di 
comando.
Suggerimento: si usi una funzione per calcolare la somma dei numeri.'''

import sys 

argv = []

def Calcolo():    
    for i in range(1, len(sys.argv)):
        argv.append(float(sys.argv[i]))

    #print(argv)
    media = round((sum(argv)/(len(sys.argv) - 1)), 2)
    print("La media vale:")
    print(media)

Calcolo()
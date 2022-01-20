#Dato N un numero intero positivo, generare e visualizzare il numero successivo.

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from pydoc import doc


N = int(input("Inserisci un numero: "))
if(N < 0):
    print('Numero non valido')
    exit()
else:
    N += 1
    print("Il numero modificato è: ", N)

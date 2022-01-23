#Dato N un numero intero positivo, generare e visualizzare in ordine crescente i primi N numeri
#interi positivi. Descrivere il problema mediante flow chart

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ast import While


N = int(input("Inserisci un numero intero e positivo: "))

if(N < 0):
    print("Numero non valido")
    exit()
else:
    cont = 1
    while(cont <= N):
        print(cont)    
        cont += 1

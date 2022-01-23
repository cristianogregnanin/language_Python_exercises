#Dato N un numero intero positivo, generare e visualizzare in ordine
#crescente i numeri pari minori o uguali a N.

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

N = int(input("Inserisci un numero intero e positivo: "))

if(N < 0):
    print("Numero non valido")
    exit()
else:
    cont = 0
    while(cont <= N):
        if((cont % 2) == 0):
            print("%d = numero pari" %(cont))

        cont +=1
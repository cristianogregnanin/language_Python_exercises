'''Dati due numeri interi positivi N1 e N2 con N2>N1, generare e
visualizzare in ordine crescente i numeri interi compresi
nell'intervallo chiuso [N1,N2]. 
Descrivere il problema mediante flow chart'''

#!/usr/bin/env python
#-*- coding: utf-8 -*- 

N1 = int(input("Inserisci N1 intero e positivo: "))
N2 = int(input("Inserisci N2 intero,positivo e maggiore di N1: "))

if(N1 < 0 or N2 < 0):
    print("Valori non inseriti correttamente")
    exit()
else:
    if(N2 <= N1):
        print("Valori non inseriti correttamente")
        exit()
    else:
        num = N1
        print("I valori contenuti nell'intervallo [%d, %d] sono: " %(N1, N2))
        while(num <= N2):
            print(num)
            num +=1

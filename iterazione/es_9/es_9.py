'''Dati due numeri interi e positivi N1 e N2 con N2>N1, generare e
visualizzare in ordine decrescente i numeri compresi tra N1 e N2. '''

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
        num = N2 -1
        print("I numeri in ordine decrescente compresi tra N1 e N2 sono: ")
        while(num > N1):
            print(num)
            num -=1
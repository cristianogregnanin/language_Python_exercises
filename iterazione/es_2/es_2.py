#Dato N un numero intero positivo, generare e visualizzare in ordine crescente i primi N numeri
#interi positivi. Descrivere il problema mediante flow chart

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

while True:
    N = int(input("Inserisci un numero intero e positivo: "))

    if(N < 0):
        print("Numero non valido")
    else:
        cont = 1
        while(cont <= N):
            print(cont)    
            cont += 1
    
    risposta = int(input("Vuoi ripetere il programma?\nInserisci il numero dell'azione che vuoi effettuare\n1)Continua\n2)Esci\n"))
    if(risposta == 2):
        break

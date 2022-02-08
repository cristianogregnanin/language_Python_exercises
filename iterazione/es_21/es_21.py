#!/usr/bin/env python
#-*- coding: utf-8 -*- 

'''Dato un numero intero positivo N verificare se N è un numero primo.'''

while True:
    num = int(input("Inserisci un numero intero positivo: "))  
    if num > 1:
        #iterazione che va da 2 a n/2
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print("%d non è un numero primo" %(num))
                break
        else:
            print("%d è un numero primo" %(num))
    
    else:
        print("%d non è un numero primo" %(num))
    
    risposta = int(input("Vuoi ripetere il programma?\nInserisci il numero dell'azione che vuoi effettuare\n1)Continua\n2)Esci\n"))
    if(risposta == 2):
        break

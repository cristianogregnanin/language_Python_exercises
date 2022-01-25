#!/usr/bin/env python
#-*- coding: utf-8 -*- 

'''Dato un numero intero positivo N verificare se N è un numero primo.'''

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
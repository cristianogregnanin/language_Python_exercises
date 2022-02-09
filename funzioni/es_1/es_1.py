#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Inserire():
    while True:
        num = int(input("Inserire un numero positivo\n"))
        if num <= 0:
            print("Errore, il numero inserito è minore o uguale a 0.")
        else: return num

num1 = Inserire()
num2 = Inserire()

print(num1 + num2)

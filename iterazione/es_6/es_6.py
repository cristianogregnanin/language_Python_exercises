#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    num = int(input("Inserire un numero intero positivo\n"))
    if num < 0:
        print("Errore, il numero inserito e' erratto")
    else: break

opposto = num * -1
while opposto <= num:
    print(opposto)
    opposto += 1
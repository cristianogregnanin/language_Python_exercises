#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    num = int(input("Inserire un numero intero strettamente positivo\n"))
    if num <= 0:
        print("Errore, hai inserito un numero errato")
    else: break

add1 = 0
add2 = num
while add1 <= (num / 2):
    print("%d %d" %(add1, add2))
    add1 += 1
    add2 -= 1
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

terni = [[0 for x in range(3)] for y in range(1)]
indice = 0
massimo = 0
minimo = -1
while True:
    ternoInput = [[0 for x in range(3)] for y in range(1)]
    ternoInput[0][0] = int(input("Inserire il primo numero del terno\n"))
    ternoInput[0][1] = int(input("Inserire il secondo numero del terno\n"))
    ternoInput[0][2] = int(input("Inserire il terzo numero del terno\n"))

    for numero in range(len(ternoInput[0])):
        if ternoInput[0][numero] < 0:
            print("Errore, hai inserito un numero negativo")
            #si calcolano il massimo ed il minimo
            for x in range(len(terni)):
                if terni[x][0] < terni[x][1] and terni[x][1] < terni[x][2]:
                    if terni[x][2] > massimo:
                        massimo = terni[x][2]
                    if minimo == -1 or terni[x][0] < minimo:#si deve valorizzare il minimo la prima volta che i numeri del terno sono in ordine strettamente crescente
                        minimo = terni[x][0]
                indice += 1
            #si visualizzano il massimo ed il minimo
            print("Il minimo vale %d, il massimo vale %d" %(minimo, massimo))
            break
        else:
            terni + ternoInput
            

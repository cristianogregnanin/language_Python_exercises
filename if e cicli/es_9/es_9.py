#!/usr/bin/env python
# -*- coding: utf-8 -*- 

terni = []
indice = 0
massimo = 0
minimo = -1

while True:
    ternoInput = [None] * 3
    ternoInput[0] = int(input("Inserire il primo numero del terno\n"))
    ternoInput[1] = int(input("Inserire il secondo numero del terno\n"))
    ternoInput[2] = int(input("Inserire il terzo numero del terno\n"))

    if ternoInput[0] < 0 or ternoInput[1] < 0 or ternoInput[2] < 0:
        print("Errore, hai inserito un numero negativo")
        break
    else:
        terni += ternoInput
        print("Hai inserito i numeri del terno correttamente")

#si controlla che sia stato inserito correttamente alemeno un terno
if len(terni)  > 0:
    #si calcolano il massimo ed il minimo
    while indice < len(terni) -1:
        terno = terni[indice : indice+3]
        if terno[0] < terno[1] and terno[1] < terno[2]:
            if terno[2] > massimo:
                massimo = terno[2]
            if minimo == -1 or terno[0] < minimo:#si deve valorizzare il minimo la prima volta che i numeri del terno sono in ordine strettamente crescente
                minimo = terno[0]
        indice += 3
    #si visualizzano il massimo ed il minimo
    print("Il minimo vale %d, il massimo vale %d" %(minimo, massimo))
else:
    print("Nessun terno inserito e' in ordine strettamente crescente")
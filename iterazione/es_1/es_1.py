#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Dato N un numero intero positivo, generare e visualizzare il numero successivo.
#Eseguire con l'esegui di vscode

while True:
    N = int(input("Inserisci un numero: "))
    if(N < 0):
        print('Numero non valido')
    else:
        N += 1
        print("Il numero modificato: %d" %(N))
    
    risposta = int(input("Vuoi ripetere il programma?\nInserisci il numero dell'azione che vuoi effettuare\n1)Continua\n2)Esci\n"))
    if(risposta == 2):
        break

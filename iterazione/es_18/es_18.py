#!/usr/bin/env python
#-*- coding: utf-8 -*- 

'''Data una misura di tempo espressa in secondi S1, convertirla in ore H,
minuti M e secondi S.
Descrivere il problema mediante flow chart. 
Esempio: se il numero dei secondi è 1630, si dovrà ottenere, in uscita
dal programma, 0h 27m 10s.'''

while True:
    sec = int(input("Inserisci i secondi da convertire: "))
    if(sec < 0):
        print("Secondi non validi")
        exit()
    else:
        secondi = sec %(24 * 3600)
        ore = sec / 3600
        secondi %= 3600
        minuti = secondi / 60
        secondi %= 60
        print("%dh %dm %ds" %(ore, minuti, secondi))

    risposta = int(input("Vuoi ripetere il programma?\nInserisci il numero dell'azione che vuoi effettuare\n1)Continua\n2)Esci\n"))
    if(risposta == 2):
        break
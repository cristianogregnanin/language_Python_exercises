#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Studente:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

f = open("studenti.txt", 'r')
studenti = []
etaMedia = 0
while True:
    line = f.readline()
    if line == "":
        break
    else:
        studenti.append(Studente(line.split(' ')[0], line.split(' ')[1], int(line.split(' ')[2])))
        etaMedia += int(line.split(' ')[2])

indexVecchio = 0
i = 0
while i < len(studenti):
    if studenti[i].eta > studenti[indexVecchio].eta:
        indexVecchio = i
    i += 1
etaMedia /= len(studenti)
print("Il nome e cognome del piu' vecchio studente e' %s %s, e la media dell'eta' vale %f" %(studenti[indexVecchio].nome, studenti[indexVecchio].cognome, etaMedia))
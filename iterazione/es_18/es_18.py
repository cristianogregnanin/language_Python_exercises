#!/usr/bin/env python
#-*- coding: utf-8 -*-

s=int(input("Inserisci il numero di secondi\n"))

m=int(s/60)
s=int(s%60)
o=int(m/60)
m=int(m%60)

print(o,m,s)

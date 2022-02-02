#!/usr/bin/env python
#-*- coding: utf-8 -*-

n1=int(input("Inserisci il numero da analizzare\n"))

for i in range(1,int(n1/2)+1):
    n2=n1-i
    print("\n%d + %d"%(i,n2))
  